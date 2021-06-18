Fetch alerts as incidents and leverage Covalence API
This integration was integrated and tested with version xx of Covalence
## Configure Covalence on Cortex XSOAR

1. Navigate to **Settings** > **Integrations** > **Servers & Services**.
2. Search for Covalence.
3. Click **Add instance** to create and configure a new integration instance.

    | **Parameter** | **Description** | **Required** |
    | --- | --- | --- |
    | Broker | Set to true if connections are made through a broker | True |
    | Host | Covalence's host \(IP or domain\) or broker's socket \(ip:port\) if using broker | True |
    | Credentials |  | True |
    | Verify SSL | If set to false, will trust any certificate \(not secure\) | False |
    | Timeout | Timeout in seconds | False |
    | First run time range | When fetching incidents for the first time, this parameter specifies in days how far the integration looks for incidents. For instance if set to "2", it will pull all alerts in Covalence for the last 2 days and will create corresponding incidents. | False |
    | Fetch limit | Maximum number of alerts to be fetch per fetch command. It is advised to not fetch more than 200 alerts. | False |
    | Use system proxy settings |  | False |

4. Click **Test** to validate the URLs, token, and connection.
## Commands
You can execute these commands from the Cortex XSOAR CLI, as part of an automation, or in a playbook.
After you successfully execute a command, a DBot message appears in the War Room with the command details.
### covalence-list-alerts
***
Lists Covalence alerts


#### Base Command

`covalence-list-alerts`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| target_org | Only required in broker mode, used to target a specific organization: target_org="Acme Corporation". | Optional | 
| max_count | Maximum number of alerts to be returned, if none provided will be set to 1000. | Optional | 
| initial_index | Initial index where to start listing alerts. | Optional | 
| alert_type | Alert type to be listed. | Optional | 
| alert_time_min | Minimal alert time in %Y-%m-%dT%H:%M:%S format and UTC time zone. | Optional | 
| alert_time_max | Maximal alert time in %Y-%m-%dT%H:%M:%S format and UTC time zone. | Optional | 
| advanced_filter | Advanced filter query. | Optional | 
| details | if details=true, will return the complete response from Covalence API. | Optional | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Covalence.Alert..acknowledgedStatus | String |  | 
| Covalence.Alert..alertCount | Number |  | 
| Covalence.Alert..alertHash | String |  | 
| Covalence.Alert..analystDescription | String |  | 
| Covalence.Alert..analystTitle | String |  | 
| Covalence.Alert..assignee | String |  | 
| Covalence.Alert..blacklistDetails.blacklistedEntity | String |  | 
| Covalence.Alert..blacklistDetails.bytesIn | Number |  | 
| Covalence.Alert..blacklistDetails.bytesOut | Number |  | 
| Covalence.Alert..blacklistDetails.listLabels | String |  | 
| Covalence.Alert..blacklistDetails.listUuids | String |  | 
| Covalence.Alert..createdTime | Number |  | 
| Covalence.Alert..destCiscoUmbrellaRanking | Number |  | 
| Covalence.Alert..destCiscoUmbrellaTopLevelDomainRanking | Number |  | 
| Covalence.Alert..destCityName | String |  | 
| Covalence.Alert..destCountryName | unknown |  | 
| Covalence.Alert..destDomainName | String |  | 
| Covalence.Alert..destGeoX | Number |  | 
| Covalence.Alert..destGeoY | Number |  | 
| Covalence.Alert..destIp | String |  | 
| Covalence.Alert..destIpAttributes.k | String |  | 
| Covalence.Alert..destIpAttributes.t | Number |  | 
| Covalence.Alert..destIpAttributes.v | String |  | 
| Covalence.Alert..destMajesticMillionRanking | Number |  | 
| Covalence.Alert..destMajesticMillionTopLevelDomainRanking | Number |  | 
| Covalence.Alert..destPort | String |  | 
| Covalence.Alert..endpointAgentUuid | String |  | 
| Covalence.Alert..facility | String |  | 
| Covalence.Alert..id | String |  | 
| Covalence.Alert..isFavorite | Boolean |  | 
| Covalence.Alert..lastAlertedTime | Number |  | 
| Covalence.Alert..notes | String |  | 
| Covalence.Alert..organizationId | String |  | 
| Covalence.Alert..pcapResourceUuid | String |  | 
| Covalence.Alert..priority | unknown |  | 
| Covalence.Alert..protocol | String |  | 
| Covalence.Alert..sensorId | String |  | 
| Covalence.Alert..severity | String |  | 
| Covalence.Alert..sigEvalDetails.id | Number |  | 
| Covalence.Alert..sigEvalDetails.message | String |  | 
| Covalence.Alert..sourceCiscoUmbrellaRanking | Number |  | 
| Covalence.Alert..sourceCiscoUmbrellaTopLevelDomainRanking | Number |  | 
| Covalence.Alert..sourceCityName | String |  | 
| Covalence.Alert..sourceCountryName | String |  | 
| Covalence.Alert..sourceDomainName | String |  | 
| Covalence.Alert..sourceGeoX | Number |  | 
| Covalence.Alert..sourceGeoY | Number |  | 
| Covalence.Alert..sourceIp | String |  | 
| Covalence.Alert..sourceIpAttributes.k | String |  | 
| Covalence.Alert..sourceIpAttributes.t | Number |  | 
| Covalence.Alert..sourceIpAttributes.v | String |  | 
| Covalence.Alert..sourceMajesticMillionRanking | Number |  | 
| Covalence.Alert..sourceMajesticMillionTopLevelDomainRanking | Number |  | 
| Covalence.Alert..sourcePort | String |  | 
| Covalence.Alert..subType | String |  | 
| Covalence.Alert..title | String |  | 
| Covalence.Alert..type | String |  | 


#### Command Example
``` ```

#### Human Readable Output



### covalence-list-sensors
***
Lists Covalence sensors


#### Base Command

`covalence-list-sensors`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| target_org | Only required in broker mode, used to target a specific organization: target_org="Acme Corporation". | Optional | 
| details | if details=true, will return the complete response from Covalence API. | Optional | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Covalence.Sensors..id | String |  | 
| Covalence.Sensors..name | String |  | 
| Covalence.Sensors..isAuthorized | Boolean |  | 
| Covalence.Sensors..isNetflowGenerator | Boolean |  | 
| Covalence.Sensors..bytesIn | Number |  | 
| Covalence.Sensors..bytesOut | Number |  | 
| Covalence.Sensors..lastActive | String |  | 
| Covalence.Sensors..listeningInterfaces | String |  | 


#### Command Example
``` ```

#### Human Readable Output



### covalence-get-sensor
***
Get sensor details when provided with the sensor id


#### Base Command

`covalence-get-sensor`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| target_org | Only required in broker mode, used to target a specific organization: target_org="Acme Corporation". | Optional | 
| sensor_id | Sensor id. | Required | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Covalence.Sensor.id | String |  | 
| Covalence.Sensor.name | String |  | 
| Covalence.Sensor.isAuthorized | Boolean |  | 
| Covalence.Sensor.listeningInterfaces | String |  | 
| Covalence.Sensor.isNetflowGenerator | Boolean |  | 
| Covalence.Sensor.bytesIn | Number |  | 
| Covalence.Sensor.bytesOut | Number |  | 
| Covalence.Sensor.lastActive | String |  | 


#### Command Example
``` ```

#### Human Readable Output



### covalence-connections-summary-ip
***
List summarized connections details by IP Address


#### Base Command

`covalence-connections-summary-ip`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| target_org | Only required in broker mode, used to target a specific organization: target_org="Acme Corporation". | Optional | 
| max_count | Maximum number of connection summary by ip to be returned, if none provided will be set to 100. | Optional | 
| initial_index | Initial index where to start listing connection summaries. | Optional | 
| source_ip | source ip filter, if used only connections related to the specified source ip will be returned. | Optional | 
| start_time | Minimal time in %Y-%m-%dT%H:%M:%S format and UTC time zone. | Optional | 
| end_time | Maximal time in %Y-%m-%dT%H:%M:%S format and UTC time zone. | Optional | 
| clients_only | if "clients_only=true", only connections labeled as client connections will be returned. | Optional | 
| internal_only | if "internal_only=true", only internal connections will be returned. | Optional | 
| advanced_filter | Advanced filter query. | Optional | 
| details | if details=true, will return the complete response from Covalence API. | Optional | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Covalence.Connections..averageDuration | Number |  | 
| Covalence.Connections..bytesIn | Number |  | 
| Covalence.Connections..bytesOut | Number |  | 
| Covalence.Connections..clientServerRelationship | String |  | 
| Covalence.Connections..continuingConnectionCount | Number |  | 
| Covalence.Connections..destinationCity | String |  | 
| Covalence.Connections..destinationCountry | String |  | 
| Covalence.Connections..destinationId | String |  | 
| Covalence.Connections..destinationIpAddress | String |  | 
| Covalence.Connections..destinationMacAddress | String |  | 
| Covalence.Connections..dstDomainName | String |  | 
| Covalence.Connections..id | String |  | 
| Covalence.Connections..packetsIn | Number |  | 
| Covalence.Connections..packetsOut | Number |  | 
| Covalence.Connections..serverPortCount | Number |  | 
| Covalence.Connections..serverPorts | String |  | 
| Covalence.Connections..sourceCity | String |  | 
| Covalence.Connections..sourceCountry | String |  | 
| Covalence.Connections..sourceDomainName | String |  | 
| Covalence.Connections..sourceId | String |  | 
| Covalence.Connections..sourceIpAddress | String |  | 
| Covalence.Connections..sourceMacAddress | String |  | 
| Covalence.Connections..terminatedConnectionCount | Number |  | 
| Covalence.Connections..totalDuration | Number |  | 


#### Command Example
``` ```

#### Human Readable Output



### covalence-connections-summary-port
***
List summarized connections details by Port


#### Base Command

`covalence-connections-summary-port`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| target_org | Only required in broker mode, used to target a specific organization: target_org="Acme Corporation". | Optional | 
| max_count | Maximum number of connection summary by port to be returned, if none provided will be set to 100. | Optional | 
| initial_index | Initial index where to start listing connection summaries. | Optional | 
| source_ip | source ip filter, only connections related to the specified source ip will be returned. | Required | 
| start_time | Minimal time in %Y-%m-%dT%H:%M:%S format and UTC time zone. | Optional | 
| end_time | Maximal time in %Y-%m-%dT%H:%M:%S format and UTC time zone. | Optional | 
| clients_only | if "clients_only=true", only connections labeled as client connections will be returned. | Optional | 
| internal_only | if "internal_only=true", only internal connections will be returned. | Optional | 
| advanced_filter | Advanced filter query. | Optional | 
| details | if details=true, will return the complete response from Covalence API. | Optional | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Covalence.Connections..averageDuration | Number |  | 
| Covalence.Connections..bytesIn | Number |  | 
| Covalence.Connections..bytesOut | Number |  | 
| Covalence.Connections..continuingConnectionCount | Number |  | 
| Covalence.Connections..destinationCity | String |  | 
| Covalence.Connections..destinationCountry | String |  | 
| Covalence.Connections..destinationId | String |  | 
| Covalence.Connections..destinationIpAddress | String |  | 
| Covalence.Connections..destinationMacAddress | String |  | 
| Covalence.Connections..dstDomainName | String |  | 
| Covalence.Connections..endTime | Date |  | 
| Covalence.Connections..id | String |  | 
| Covalence.Connections..packetsIn | Number |  | 
| Covalence.Connections..packetsOut | Number |  | 
| Covalence.Connections..protocol | String |  | 
| Covalence.Connections..serverPort | Number |  | 
| Covalence.Connections..sourceCity | String |  | 
| Covalence.Connections..sourceCountry | String |  | 
| Covalence.Connections..sourceDomainName | String |  | 
| Covalence.Connections..sourceId | String |  | 
| Covalence.Connections..sourceIpAddress | String |  | 
| Covalence.Connections..sourceMacAddress | String |  | 
| Covalence.Connections..startTime | Date |  | 
| Covalence.Connections..terminatedConnectionCount | Number |  | 
| Covalence.Connections..totalDuration | Number |  | 


#### Command Example
``` ```

#### Human Readable Output



### covalence-list-dns-resolutions
***
List summarized connections details by Port


#### Base Command

`covalence-list-dns-resolutions`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| target_org | Only required in broker mode, used to target a specific organization: target_org="Acme Corporation". | Optional | 
| max_count | Maximum number of DNS resolutions to be returned, if none provided will be set to 100. | Optional | 
| initial_index | Initial index where to start listing DNS resolutions. | Optional | 
| request_time_after | Minimal time in %Y-%m-%dT%H:%M:%S format and UTC time zone. | Optional | 
| request_time_before | Maximal time in %Y-%m-%dT%H:%M:%S format and UTC time zone. | Optional | 
| domain_name | Domain name filter, if used will only return DNS resolutions from the specified domain name. | Optional | 
| resolved_ip | IP filter, if used will only return DNS resolutions to the specified IP. | Optional | 
| request_origin_ip | Source IP filter, if used will only return DNS resolutions originating from the specified IP. | Optional | 
| nameserver_ip | Nameserver IP filter, if used will only return DNS resolutions involving the specified nameserver IP. | Optional | 
| advanced_filter | Advanced filter query. | Optional | 
| details | if details=true, will return the complete response from Covalence API. | Optional | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Covalence.DNSResolutions..id | String |  | 
| Covalence.DNSResolutions..domainName | String |  | 
| Covalence.DNSResolutions..resolvedIp | String |  | 
| Covalence.DNSResolutions..requestOriginIp | String |  | 
| Covalence.DNSResolutions..nameserverIp | String |  | 
| Covalence.DNSResolutions..nodeLabel | String |  | 
| Covalence.DNSResolutions..requestTime | Number |  | 
| Covalence.DNSResolutions..byteCount | Number |  | 
| Covalence.DNSResolutions..pktCount | Number |  | 


#### Command Example
``` ```

#### Human Readable Output



### covalence-list-internal-networks
***
List internal networks


#### Base Command

`covalence-list-internal-networks`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| target_org | Only required in broker mode, used to target a specific organization: target_org="Acme Corporation". | Optional | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Covalence.InternalNetworks..cidr | String |  | 
| Covalence.InternalNetworks..notes | String |  | 


#### Command Example
``` ```

#### Human Readable Output



### covalence-set-internal-networks
***
Set internal networks


#### Base Command

`covalence-set-internal-networks`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| target_org | Only required in broker mode, used to target a specific organization: target_org="Acme Corporation". | Optional | 
| cidr | The network to be set as internal in CIDR notation. | Required | 
| notes | Comment notes associated with the network, notes must be inside quotes. | Required | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Covalence.InternalNetworks..cidr | String |  | 
| Covalence.InternalNetworks..notes | String |  | 


#### Command Example
``` ```

#### Human Readable Output



### covalence-list-endpoint-agents
***
List endpoint agents


#### Base Command

`covalence-list-endpoint-agents`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| target_org | Only required in broker mode, used to target a specific organization: target_org="Acme Corporation". | Optional | 
| advanced_filter | Advanced filter query, if used any other parameters provided to the command will be ignored. | Optional | 
| details | if details=true, will return the complete response from Covalence API. | Optional | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Covalence.EndpointAgents..agentUuid | String |  | 
| Covalence.EndpointAgents..agentVersion | String |  | 
| Covalence.EndpointAgents..firstSeenTime | Date |  | 
| Covalence.EndpointAgents..lastSeenTime | Date |  | 
| Covalence.EndpointAgents..lastSessionUser | String |  | 
| Covalence.EndpointAgents..isMobile | Boolean |  | 
| Covalence.EndpointAgents..isConnected | Boolean |  | 
| Covalence.EndpointAgents..coreVersion | String |  | 
| Covalence.EndpointAgents..coreArchitecture | String |  | 
| Covalence.EndpointAgents..coreOs | String |  | 
| Covalence.EndpointAgents..operatingSystem | String |  | 
| Covalence.EndpointAgents..hostName | String |  | 
| Covalence.EndpointAgents..hardwareVendor | String |  | 
| Covalence.EndpointAgents..hardwareModel | String |  | 
| Covalence.EndpointAgents..arch | String |  | 
| Covalence.EndpointAgents..osDistro | String |  | 
| Covalence.EndpointAgents..osVersion | String |  | 
| Covalence.EndpointAgents..kernelVersion | String |  | 
| Covalence.EndpointAgents..operatingSystemReleaseId | String |  | 
| Covalence.EndpointAgents..ipAddress | String |  | 
| Covalence.EndpointAgents..secondaryIpAddress | String |  | 
| Covalence.EndpointAgents..ipAddresses | String |  | 
| Covalence.EndpointAgents..serialNumber | String |  | 
| Covalence.EndpointAgents..deviceIdentifier | String |  | 
| Covalence.EndpointAgents..cpuArchitectureEnum | String |  | 


#### Command Example
``` ```

#### Human Readable Output



### covalence-find-endpoint-agents-by-user
***
List endpoint agents where the last session user is the one provided as parameter


#### Base Command

`covalence-find-endpoint-agents-by-user`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| target_org | Only required in broker mode, used to target a specific organization: target_org="Acme Corporation". | Optional | 
| user | User filter. | Required | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Covalence.EndpointAgents..agentUuid | String |  | 
| Covalence.EndpointAgents..agentVersion | String |  | 
| Covalence.EndpointAgents..firstSeenTime | Date |  | 
| Covalence.EndpointAgents..lastSeenTime | Date |  | 
| Covalence.EndpointAgents..lastSessionUser | String |  | 
| Covalence.EndpointAgents..isMobile | Boolean |  | 
| Covalence.EndpointAgents..isConnected | Boolean |  | 
| Covalence.EndpointAgents..coreVersion | String |  | 
| Covalence.EndpointAgents..coreArchitecture | String |  | 
| Covalence.EndpointAgents..coreOs | String |  | 
| Covalence.EndpointAgents..operatingSystem | String |  | 
| Covalence.EndpointAgents..hostName | String |  | 
| Covalence.EndpointAgents..hardwareVendor | String |  | 
| Covalence.EndpointAgents..hardwareModel | String |  | 
| Covalence.EndpointAgents..arch | String |  | 
| Covalence.EndpointAgents..osDistro | String |  | 
| Covalence.EndpointAgents..osVersion | String |  | 
| Covalence.EndpointAgents..kernelVersion | String |  | 
| Covalence.EndpointAgents..operatingSystemReleaseId | String |  | 
| Covalence.EndpointAgents..ipAddress | String |  | 
| Covalence.EndpointAgents..secondaryIpAddress | String |  | 
| Covalence.EndpointAgents..ipAddresses | String |  | 
| Covalence.EndpointAgents..serialNumber | String |  | 
| Covalence.EndpointAgents..deviceIdentifier | String |  | 
| Covalence.EndpointAgents..cpuArchitectureEnum | String |  | 


#### Command Example
``` ```

#### Human Readable Output



### covalence-find-endpoint-agents-by-uuid
***
Find the endpoint agent with the UUID provided as parameter


#### Base Command

`covalence-find-endpoint-agents-by-uuid`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| target_org | Only required in broker mode, used to target a specific organization: target_org="Acme Corporation". | Optional | 
| uuid | Endpoint agent UUID. | Required | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Covalence.EndpointAgents..agentUuid | String |  | 
| Covalence.EndpointAgents..agentVersion | String |  | 
| Covalence.EndpointAgents..firstSeenTime | Date |  | 
| Covalence.EndpointAgents..lastSeenTime | Date |  | 
| Covalence.EndpointAgents..lastSessionUser | String |  | 
| Covalence.EndpointAgents..isMobile | Boolean |  | 
| Covalence.EndpointAgents..isConnected | Boolean |  | 
| Covalence.EndpointAgents..coreVersion | String |  | 
| Covalence.EndpointAgents..coreArchitecture | String |  | 
| Covalence.EndpointAgents..coreOs | String |  | 
| Covalence.EndpointAgents..operatingSystem | String |  | 
| Covalence.EndpointAgents..hostName | String |  | 
| Covalence.EndpointAgents..hardwareVendor | String |  | 
| Covalence.EndpointAgents..hardwareModel | String |  | 
| Covalence.EndpointAgents..arch | String |  | 
| Covalence.EndpointAgents..osDistro | String |  | 
| Covalence.EndpointAgents..osVersion | String |  | 
| Covalence.EndpointAgents..kernelVersion | String |  | 
| Covalence.EndpointAgents..operatingSystemReleaseId | String |  | 
| Covalence.EndpointAgents..ipAddress | String |  | 
| Covalence.EndpointAgents..secondaryIpAddress | String |  | 
| Covalence.EndpointAgents..ipAddresses | String |  | 
| Covalence.EndpointAgents..serialNumber | String |  | 
| Covalence.EndpointAgents..deviceIdentifier | String |  | 
| Covalence.EndpointAgents..cpuArchitectureEnum | String |  | 


#### Command Example
``` ```

#### Human Readable Output



### covalence-search-endpoint-process
***
Search processes by name or advanced filter, at least one parameter is required


#### Base Command

`covalence-search-endpoint-process`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| target_org | Only required in broker mode, used to target a specific organization: target_org="Acme Corporation". | Optional | 
| name | Process name. | Optional | 
| advanced_filter | Advanced filter query. | Optional | 
| details | if details=true, will return the complete response from Covalence API. | Optional | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Covalence.EndpointProcess..id | Number |  | 
| Covalence.EndpointProcess..agentUuid | String |  | 
| Covalence.EndpointProcess..processName | String |  | 
| Covalence.EndpointProcess..processPath | String |  | 
| Covalence.EndpointProcess..parentProcessName | String |  | 
| Covalence.EndpointProcess..parentProcessPath | String |  | 
| Covalence.EndpointProcess..commandLine | String |  | 
| Covalence.EndpointProcess..username | String |  | 
| Covalence.EndpointProcess..firstSeenTime | Date |  | 
| Covalence.EndpointProcess..lastSeenTime | Date |  | 
| Covalence.EndpointProcess..lastEndTime | Date |  | 
| Covalence.EndpointProcess..seenCount | Number |  | 
| Covalence.EndpointProcess..activeCount | Number |  | 


#### Command Example
``` ```

#### Human Readable Output



### covalence-search-endpoint-installed-software
***
Search for endpoint installed software


#### Base Command

`covalence-search-endpoint-installed-software`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| target_org | Only required in broker mode, used to target a specific organization: target_org="Acme Corporation". | Optional | 
| name | The name of installed software, quotes are required is space character is used. At least one parameter is required. | Required | 
| version | The version of installed software. | Optional | 
| advanced_filter | Advanced filter query. | Optional | 
| details | if details=true, will return the complete response from Covalence API. | Optional | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Covalence.EndpointSoftware..arch | Number |  | 
| Covalence.EndpointSoftware..type | Number |  | 
| Covalence.EndpointSoftware..packageManager | Number |  | 
| Covalence.EndpointSoftware..installTimestamp | Date |  | 
| Covalence.EndpointSoftware..uninstallTimestamp | Date |  | 
| Covalence.EndpointSoftware..name | String |  | 
| Covalence.EndpointSoftware..version | String |  | 
| Covalence.EndpointSoftware..vendor | String |  | 
| Covalence.EndpointSoftware..installPath | String |  | 
| Covalence.EndpointSoftware..appDataPath | String |  | 
| Covalence.EndpointSoftware..sharedDataPath | String |  | 
| Covalence.EndpointSoftware..installedForUser | String |  | 
| Covalence.EndpointSoftware..installSource | String |  | 
| Covalence.EndpointSoftware..id | Number |  | 
| Covalence.EndpointSoftware..agentUuid | String |  | 
| Covalence.EndpointSoftware..softwareNotifyAction | String |  | 


#### Command Example
``` ```

#### Human Readable Output



### covalence-list-organizations
***
List monitored organizations, only available in broker mode


#### Base Command

`covalence-list-organizations`
#### Input

There are no input arguments for this command.

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Covalence.Organization..org_name | String |  | 


#### Command Example
``` ```

#### Human Readable Output

