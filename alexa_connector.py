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
import base64
import datetime
import hashlib
import hmac
import urllib
import simplejson as json
import xmltodict
import requests


class AlexaConnector(BaseConnector):
    ACTION_ID_TEST_ASSET_CONNECTIVITY = "test_connectivity"
    ACTION_ID_LOOKUP_URL = "lookup_url"

    def __init__(self):

        super(AlexaConnector, self).__init__()

    def initialize(self):

        config = self.get_config()

        self._access_id = config[ALEXA_CONFIG_ACCESS_ID]
        self._secret_key = config[ALEXA_CONFIG_SECRET_KEY]

        return phantom.APP_SUCCESS

    def _make_rest_call(self, params):

        params["AWSAccessKeyId"] = self._access_id
        params["SignatureMethod"] = "HmacSHA1"
        params["SignatureVersion"] = "2"
        params["Timestamp"] = self._get_timestamp()
        params["Signature"] = self._sign(params)

        url = "https://{0}/".format(ALEXA_AWIS_HOST)

        try:
            response = requests.get(url, verify=self.get_config().get("verify_server_cert"), params=params)
        except Exception as e:
            return (phantom.APP_ERROR, "Could not make REST call {}".format(e))

        if (response.status_code != 200):
            return (phantom.APP_ERROR, "REST call failed. {}".format((xmltodict.parse(response.text))))

        try:
            # Someone tell my why this isn't a json response.  Now I have to import xmltodict to parse it...
            resp_json = xmltodict.parse(response.text)
        except Exception:
            return (phantom.APP_ERROR, "Error while parsing response to JSON. {}", format(response))

        return phantom.APP_SUCCESS, resp_json

    def _get_timestamp(self):
        '''
        Gets the current timestamp in a format that is specified by AWIS
        :return: timestamp in str
        '''
        return datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")

    def _sign(self, params):
        '''
        Gets an AWIS-specific signature to be used in the REST call
        :return: signature
        '''

        # Builds the string for the message, as required by AWIS.
        message = "\n".join(["GET", ALEXA_AWIS_HOST, "/", self._urlencode(params)])

        # Creates a signature based upon the access key and the message, hashed with sha1.
        hmac_signature = hmac.new(str(self._secret_key), message, digestmod=hashlib.sha1)

        # Pulls the encoded signature from the signature.
        signature = base64.b64encode(hmac_signature.digest())

        return signature

    def _urlencode(self, params):
        # Params must be sorted alphabetically before being encoded.

        params = [(key, params[key]) for key in sorted(params.keys())]

        return urllib.urlencode(params)

    def _test_connectivity(self):
        self.save_progress("Querying AWIS...")
        self.save_progress("Verify server certificate: {}".format(self.get_config().get("verify_server_cert")))
        param = {
            "Action": "UrlInfo",
            "Url": "http://www.amazon.com/",
            "ResponseGroup": ALEXA_ACTION_RESPONSE_GROUP
        }

        ret_val, response = self._make_rest_call(param)

        if (phantom.is_fail(ret_val)):

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

        if (phantom.is_fail(ret_val)):
            return (action_result.set_status(phantom.APP_ERROR, "Error retrieving information", response))

        action_result.add_data(response)

        rank = response['aws:UrlInfoResponse']['aws:Response']['aws:UrlInfoResult']['aws:Alexa']['aws:TrafficData']['aws:Rank']

        action_result.set_summary({"rank": rank})

        return (action_result.set_status(phantom.APP_SUCCESS))

    def handle_action(self, params):

        action = self.get_action_identifier()

        ret_val = phantom.APP_SUCCESS

        if (action == self.ACTION_ID_LOOKUP_URL):
            ret_val = self._lookup_url(params)
        elif (action == self.ACTION_ID_TEST_ASSET_CONNECTIVITY):
            ret_val = self._test_connectivity()
        return ret_val


if __name__ == '__main__':
    '''
    This block gets executed during debugging.  Does not affect regular action handling

    '''

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
