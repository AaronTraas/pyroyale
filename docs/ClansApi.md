# pyroyale.ClansApi

All URIs are relative to *https://api.clashroyale.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_clan**](ClansApi.md#get_clan) | **GET** /clans/{clanTag} | Get clan information
[**get_clan_members**](ClansApi.md#get_clan_members) | **GET** /clans/{clanTag}/members | List clan members
[**get_clan_war_log**](ClansApi.md#get_clan_war_log) | **GET** /clans/{clanTag}/warlog | Retrieve clan&#x27;s clan war log
[**get_current_war**](ClansApi.md#get_current_war) | **GET** /clans/{clanTag}/currentwar | Information about clan&#x27;s current clan war
[**search_clans**](ClansApi.md#search_clans) | **GET** /clans | Search clans

# **get_clan**
> Clan get_clan(clan_tag)

Get clan information

Get information about a single clan by clan tag. Clan tags can be found using clan search operation. Note that clan tags start with hash character '#' and that needs to be URL-encoded properly to work in URL, so for example clan tag '#2ABC' would become '%232ABC' in the URL. 

### Example
```python
from __future__ import print_function
import time
import pyroyale
from pyroyale.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = pyroyale.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pyroyale.ClansApi(pyroyale.ApiClient(configuration))
clan_tag = 'clan_tag_example' # str | Tag of the clan to retrieve.

try:
    # Get clan information
    api_response = api_instance.get_clan(clan_tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClansApi->get_clan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_tag** | **str**| Tag of the clan to retrieve. | 

### Return type

[**Clan**](Clan.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clan_members**
> ClanMemberList get_clan_members(clan_tag, limit=limit, after=after, before=before)

List clan members

List clan members

### Example
```python
from __future__ import print_function
import time
import pyroyale
from pyroyale.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = pyroyale.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pyroyale.ClansApi(pyroyale.ApiClient(configuration))
clan_tag = 'clan_tag_example' # str | Tag of the clan whose members to retrieve.
limit = 56 # int | Limit the number of items returned in the response. (optional)
after = 56 # int | Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 56 # int | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

try:
    # List clan members
    api_response = api_instance.get_clan_members(clan_tag, limit=limit, after=after, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClansApi->get_clan_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_tag** | **str**| Tag of the clan whose members to retrieve. | 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **int**| Return only items that occur after this marker. After marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **int**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**ClanMemberList**](ClanMemberList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clan_war_log**
> WarLog get_clan_war_log(clan_tag, limit=limit, after=after, before=before)

Retrieve clan's clan war log

Retrieve clan's clan war log

### Example
```python
from __future__ import print_function
import time
import pyroyale
from pyroyale.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = pyroyale.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pyroyale.ClansApi(pyroyale.ApiClient(configuration))
clan_tag = 'clan_tag_example' # str | Tag of the clan whose war log to retrieve.
limit = 56 # int | Limit the number of items returned in the response. (optional)
after = 56 # int | Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 56 # int | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

try:
    # Retrieve clan's clan war log
    api_response = api_instance.get_clan_war_log(clan_tag, limit=limit, after=after, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClansApi->get_clan_war_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_tag** | **str**| Tag of the clan whose war log to retrieve. | 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **int**| Return only items that occur after this marker. After marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **int**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**WarLog**](WarLog.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_war**
> WarCurrent get_current_war(clan_tag)

Information about clan's current clan war

Retrieve information about clan's current clan war

### Example
```python
from __future__ import print_function
import time
import pyroyale
from pyroyale.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = pyroyale.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pyroyale.ClansApi(pyroyale.ApiClient(configuration))
clan_tag = 'clan_tag_example' # str | Tag of the clan whose war log to retrieve.

try:
    # Information about clan's current clan war
    api_response = api_instance.get_current_war(clan_tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClansApi->get_current_war: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_tag** | **str**| Tag of the clan whose war log to retrieve. | 

### Return type

[**WarCurrent**](WarCurrent.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_clans**
> ClanSearchResult search_clans(name=name, location_id=location_id, min_members=min_members, max_members=max_members, min_score=min_score, limit=limit, after=after, before=before)

Search clans

Search all clans by name and/or filtering the results using various criteria. At least one filtering criteria must be defined and if name is used as part of search, it is required to be at least three characters long. It is not possible to specify ordering for results so clients should not rely on any specific ordering as that may change in the future releases of the API. 

### Example
```python
from __future__ import print_function
import time
import pyroyale
from pyroyale.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = pyroyale.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pyroyale.ClansApi(pyroyale.ApiClient(configuration))
name = 'name_example' # str | Search clans by name. If name is used as part of search query, it needs to be at least three characters long. Name search parameter is interpreted as wild card search, so it may appear anywhere in the clan name.  (optional)
location_id = 56 # int | Filter by clan location identifier. For list of available locations, refer to getLocations operation.  (optional)
min_members = 56 # int | Filter by minimum amount of clan members.  (optional)
max_members = 56 # int | Filter by maximum amount of clan members.  (optional)
min_score = 56 # int | Filter by minimum amount of clan score.  (optional)
limit = 56 # int | Limit the number of items returned in the response.  (optional)
after = 56 # int | Return only items that occur after this marker. After marker can be found from theresponse, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 56 # int | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

try:
    # Search clans
    api_response = api_instance.search_clans(name=name, location_id=location_id, min_members=min_members, max_members=max_members, min_score=min_score, limit=limit, after=after, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClansApi->search_clans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Search clans by name. If name is used as part of search query, it needs to be at least three characters long. Name search parameter is interpreted as wild card search, so it may appear anywhere in the clan name.  | [optional] 
 **location_id** | **int**| Filter by clan location identifier. For list of available locations, refer to getLocations operation.  | [optional] 
 **min_members** | **int**| Filter by minimum amount of clan members.  | [optional] 
 **max_members** | **int**| Filter by maximum amount of clan members.  | [optional] 
 **min_score** | **int**| Filter by minimum amount of clan score.  | [optional] 
 **limit** | **int**| Limit the number of items returned in the response.  | [optional] 
 **after** | **int**| Return only items that occur after this marker. After marker can be found from theresponse, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **int**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**ClanSearchResult**](ClanSearchResult.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

