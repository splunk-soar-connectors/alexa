# --
# File: alexa_connector.py
#
# Copyright (c) Phantom Cyber Corporation, 2016-2017
#
# This unpublished material is proprietary to Phantom Cyber.
# All rights reserved. The methods and
# techniques described herein are considered trade secrets
# and/or confidential. Reproduction or distribution, in whole
# or in part, is forbidden except by express written permission
# of Phantom Cyber.
#
# --

# Phantom imports
import phantom.app as phantom
from phantom.base_connector import BaseConnector
from phantom.action_result import ActionResult

# THIS Connector imports
from alexa_consts import *

# Any imports that this app may need that are not phantom-based or app-based
from urllib import urlencode
import datetime
import hashlib
import hmac
import xmltodict
import requests
import simplejson as json


class AlexaConnector(BaseConnector):
    ACTION_ID_TEST_ASSET_CONNECTIVITY = "test_connectivity"
    ACTION_ID_LOOKUP_URL = "lookup_url"

    def __init__(self):

        super(AlexaConnector, self).__init__()

        self._access_id = None
        self._secret_key = None

    def initialize(self):

        config = self.get_config()

        self._access_id = config[ALEXA_CONFIG_ACCESS_ID]
        self._secret_key = config[ALEXA_CONFIG_SECRET_KEY]

        return phantom.APP_SUCCESS

    def _make_rest_call(self, params):

        url, headers = self._sign(params)

        try:
            response = requests.get(url,
                                    headers=headers,
                                    verify=True)
        except Exception as e:
            return phantom.APP_ERROR, "Could not make REST call {}".format(e)

        if response.status_code != 200:
            return phantom.APP_ERROR, "REST call failed. {}".format(response.text)

        try:
            resp_json = xmltodict.parse(response.text)
        except Exception:
            return phantom.APP_ERROR, "Error while parsing response to JSON. {}", format(response)

        return phantom.APP_SUCCESS, resp_json

    def _get_signing_key(self, key, credential_list):
        """ Process the key and other credentials to build an AWS signing key.

        Args:
            key (str): AWS secret key
            credential_list (list): list of additional credentials needed to sign the request

        Returns:
            key (HMAC Digest): Signing key
        """
        key = ('AWS4' + key).encode('utf-8')
        for credential in credential_list:
            key = hmac.new(key, credential.encode('utf-8'), hashlib.sha256).digest()
            self.debug_print(credential)
        return key

    def _sign(self, request_params):
        """ Create URL and signature headers based on AWS V4 signing process.

        Args:
            request_params (dict): Parameters for request

        Returns:
            request_url (str): URL to use in request, including params
            headers (dict): Headers needed to make AWS request
        """
        method = 'GET'
        service = 'awis'
        region = 'us-west-1'
        endpoint = '{}.{}.amazonaws.com'.format(service, region)
        request_parameters = urlencode([(key, request_params[key]) for key in sorted(request_params.keys())])

        # Create a date for headers and the credential string
        t = datetime.datetime.utcnow()
        amzdate = t.strftime('%Y%m%dT%H%M%SZ')
        datestamp = t.strftime('%Y%m%d')  # Date w/o time, used in credential scope

        # Create canonical request
        canonical_uri = '/api'
        canonical_querystring = request_parameters
        canonical_headers = 'host:{}\nx-amz-date:{}\n'.format(endpoint, amzdate)
        signed_headers = 'host;x-amz-date'

        payload_hash = hashlib.sha256(''.encode('utf8')).hexdigest()
        canonical_request = '\n'.join([method, canonical_uri, canonical_querystring, canonical_headers, signed_headers, payload_hash])

        # Create string to sign
        credential_list = [datestamp, region, service, 'aws4_request']
        credential_scope = '/'.join(credential_list)
        algorithm = 'AWS4-HMAC-SHA256'
        string_to_sign = '\n'.join([algorithm, amzdate, credential_scope, hashlib.sha256(canonical_request.encode('utf8')).hexdigest()])

        # Calculate signature
        signing_key = self._get_signing_key(self._secret_key, credential_list)

        # Sign the string_to_sign using the signing_key
        signature = hmac.new(signing_key, string_to_sign.encode('utf-8'), hashlib.sha256).hexdigest()

        # Add signing information to the request
        authorization_header = '{} Credential={}/{}, SignedHeaders={}, Signature={}'.format(algorithm, self._access_id, credential_scope, signed_headers, signature)
        headers = {'X-Amz-Date': amzdate, 'Authorization': authorization_header, 'Content-Type': 'application/xml', 'Accept': 'application/xml'}

        # Create request url
        request_url = 'https://{}{}?{}'.format(endpoint, canonical_uri, canonical_querystring)
        return request_url, headers

    def _test_connectivity(self):
        self.save_progress("Querying AWIS...")
        param = {
            "Action": "UrlInfo",
            "Url": "https://www.amazon.com/",
            "ResponseGroup": ALEXA_ACTION_RESPONSE_GROUP
        }

        ret_val, response = self._make_rest_call(param)

        if phantom.is_fail(ret_val):

            self.save_progress("Rest call failed. {}".format(response))

            return phantom.APP_ERROR

        self.save_progress("Rest call succeeded")

        return self.set_status_save_progress(phantom.APP_SUCCESS, "Test Connectivity succeeded")

    def _lookup_url(self, params):

        action_result = self.add_action_result(ActionResult(params))

        url = params[ALEXA_JSON_URL]

        param = {
            "Action": "UrlInfo",
            "Url": url,
            "ResponseGroup": ALEXA_ACTION_RESPONSE_GROUP
        }

        ret_val, response = self._make_rest_call(param)

        if phantom.is_fail(ret_val):
            return action_result.set_status(phantom.APP_ERROR, "Error retrieving information", response)

        action_result.add_data(response)

        rank = response['aws:UrlInfoResponse']['aws:Response']['aws:UrlInfoResult']['aws:Alexa']['aws:TrafficData']['aws:Rank']

        action_result.set_summary({"rank": rank})

        return action_result.set_status(phantom.APP_SUCCESS)

    def handle_action(self, params):

        action = self.get_action_identifier()

        ret_val = phantom.APP_SUCCESS

        if action == self.ACTION_ID_LOOKUP_URL:
            ret_val = self._lookup_url(params)
        elif action == self.ACTION_ID_TEST_ASSET_CONNECTIVITY:
            ret_val = self._test_connectivity()
        return ret_val


if __name__ == '__main__':
    """
    This block gets executed during debugging.  Does not affect regular action handling

    """

    # Imports
    import sys
    import pudb

    # Breakpoint at runtime
    pudb.set_trace()

    # The first param is the input json file
    with open(sys.argv[1]) as f:
        # Load the input json file
        in_json = f.read()
        in_json = json.loads(in_json)
        print(json.dumps(in_json, indent=' ' * 4))

        # Create the connector class object
        connector = AlexaConnector()

        # Se the member vars
        connector.print_progress_message = True

        # Call BaseConnector::_handle_action(...) to kickoff action handling.
        ret_val = connector._handle_action(json.dumps(in_json), None)

        # Dump the return value
        print ret_val

    exit(0)
