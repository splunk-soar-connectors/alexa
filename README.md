[comment]: # "Auto-generated SOAR connector documentation"
# Alexa

Publisher: Splunk  
Connector Version: 2\.0\.4  
Product Vendor: Amazon  
Product Name: Alexa  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.9\.39220  

This app implements investigative actions using Alexa Web Information Services

### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Alexa asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**access\_id** |  required  | string | Access ID
**secret\_key** |  required  | password | Secret key

### Supported Actions  
[lookup url](#action-lookup-url) - Gets information about a URL  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  

## action: 'lookup url'
Gets information about a URL

Type: **investigate**  
Read only: **True**

<p>Information this action gets\:</p><ul><li>Up to 11 related links</li><li>Up to 3 DMOZ categories</li><li>Traffic rank</li><li>Usage statistics</li><li>Title, description, and date the site was created</li><li>Whether the site is likely to contain adult content</li><li>Median load time and percent of known sites that are slower</li><li>Content language code and character\-encoding of the majority of pages</li></ul>

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**url** |  required  | URL to query | string |  `url`  `domain` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.url | string |  `url`  `domain` 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.\@xmlns\:aws | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.\@xmlns\:aws | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:OperationRequest\.aws\:RequestId | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:ResponseStatus\.\@xmlns\:aws | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:ResponseStatus\.aws\:StatusCode | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:ContentData\.aws\:AdultContent | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:ContentData\.aws\:DataUrl\.\#text | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:ContentData\.aws\:DataUrl\.\@type | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:ContentData\.aws\:Keywords | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:ContentData\.aws\:Keywords\.aws\:Keyword | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:ContentData\.aws\:Language | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:ContentData\.aws\:Language\.aws\:Locale | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:ContentData\.aws\:LinksInCount | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:ContentData\.aws\:OwnedDomains | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:ContentData\.aws\:OwnedDomains\.aws\:OwnedDomain\.\*\.aws\:Domain | string |  `domain` 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:ContentData\.aws\:OwnedDomains\.aws\:OwnedDomain\.\*\.aws\:Title | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:ContentData\.aws\:SiteData\.aws\:Description | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:ContentData\.aws\:SiteData\.aws\:OnlineSince | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:ContentData\.aws\:SiteData\.aws\:Title | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:ContentData\.aws\:Speed\.aws\:MedianLoadTime | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:ContentData\.aws\:Speed\.aws\:Percentile | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:Related\.aws\:Categories\.aws\:CategoryData\.\*\.aws\:AbsolutePath | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:Related\.aws\:Categories\.aws\:CategoryData\.\*\.aws\:Title | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:Related\.aws\:DataUrl\.\#text | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:Related\.aws\:DataUrl\.\@type | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:Related\.aws\:RelatedLinks | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:Related\.aws\:RelatedLinks\.aws\:RelatedLink\.\*\.aws\:DataUrl\.\#text | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:Related\.aws\:RelatedLinks\.aws\:RelatedLink\.\*\.aws\:DataUrl\.\@type | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:Related\.aws\:RelatedLinks\.aws\:RelatedLink\.\*\.aws\:NavigableUrl | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:Related\.aws\:RelatedLinks\.aws\:RelatedLink\.\*\.aws\:Title | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:ContributingSubdomains | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:ContributingSubdomains\.aws\:ContributingSubdomain\.\*\.aws\:DataUrl | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:ContributingSubdomains\.aws\:ContributingSubdomain\.\*\.aws\:PageViews\.aws\:PerUser | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:ContributingSubdomains\.aws\:ContributingSubdomain\.\*\.aws\:PageViews\.aws\:Percentage | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:ContributingSubdomains\.aws\:ContributingSubdomain\.\*\.aws\:Reach\.aws\:Percentage | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:ContributingSubdomains\.aws\:ContributingSubdomain\.\*\.aws\:TimeRange\.aws\:Months | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:DataUrl\.\#text | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:DataUrl\.\@type | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:Rank | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:UsageStatistics | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:UsageStatistics\.aws\:UsageStatistic\.\*\.aws\:PageViews\.aws\:PerMillion\.aws\:Delta | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:UsageStatistics\.aws\:UsageStatistic\.\*\.aws\:PageViews\.aws\:PerMillion\.aws\:Value | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:UsageStatistics\.aws\:UsageStatistic\.\*\.aws\:PageViews\.aws\:PerUser\.aws\:Delta | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:UsageStatistics\.aws\:UsageStatistic\.\*\.aws\:PageViews\.aws\:PerUser\.aws\:Value | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:UsageStatistics\.aws\:UsageStatistic\.\*\.aws\:PageViews\.aws\:Rank\.aws\:Delta | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:UsageStatistics\.aws\:UsageStatistic\.\*\.aws\:PageViews\.aws\:Rank\.aws\:Value | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:UsageStatistics\.aws\:UsageStatistic\.\*\.aws\:Rank\.aws\:Delta | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:UsageStatistics\.aws\:UsageStatistic\.\*\.aws\:Rank\.aws\:Value | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:UsageStatistics\.aws\:UsageStatistic\.\*\.aws\:Reach\.aws\:PerMillion\.aws\:Delta | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:UsageStatistics\.aws\:UsageStatistic\.\*\.aws\:Reach\.aws\:PerMillion\.aws\:Value | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:UsageStatistics\.aws\:UsageStatistic\.\*\.aws\:Reach\.aws\:Rank\.aws\:Delta | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:UsageStatistics\.aws\:UsageStatistic\.\*\.aws\:Reach\.aws\:Rank\.aws\:Value | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:UsageStatistics\.aws\:UsageStatistic\.\*\.aws\:TimeRange\.aws\:Days | string | 
action\_result\.data\.\*\.aws\:UrlInfoResponse\.aws\:Response\.aws\:UrlInfoResult\.aws\:Alexa\.aws\:TrafficData\.aws\:UsageStatistics\.aws\:UsageStatistic\.\*\.aws\:TimeRange\.aws\:Months | string | 
action\_result\.summary | string | 
action\_result\.summary\.rank | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output