# pyroyale.LocationsApi

All URIs are relative to *https://api.clashroyale.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_clan_ranking**](LocationsApi.md#get_clan_ranking) | **GET** /locations/{locationId}/rankings/clans | Get clan rankings for a specific location
[**get_clan_wars_ranking**](LocationsApi.md#get_clan_wars_ranking) | **GET** /locations/{locationId}/rankings/clanwars | Get clan war rankings for a specific location
[**get_location**](LocationsApi.md#get_location) | **GET** /locations/{locationId} | Get location information
[**get_locations**](LocationsApi.md#get_locations) | **GET** /locations | List locations
[**get_player_ranking**](LocationsApi.md#get_player_ranking) | **GET** /locations/{locationId}/rankings/players | Get player rankings for a specific location

# **get_clan_ranking**
> ClanRankingList get_clan_ranking(location_id, limit=limit, after=after, before=before)

Get clan rankings for a specific location

Get clan rankings for a specific location

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
api_instance = pyroyale.LocationsApi(pyroyale.ApiClient(configuration))
location_id = 'location_id_example' # str | Identifier of the location to retrieve.
limit = 56 # int | Limit the number of items returned in the response.  (optional)
after = 56 # int | Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 56 # int | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

try:
    # Get clan rankings for a specific location
    api_response = api_instance.get_clan_ranking(location_id, limit=limit, after=after, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_clan_ranking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| Identifier of the location to retrieve. | 
 **limit** | **int**| Limit the number of items returned in the response.  | [optional] 
 **after** | **int**| Return only items that occur after this marker. After marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **int**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**ClanRankingList**](ClanRankingList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clan_wars_ranking**
> ClanWarsRankingList get_clan_wars_ranking(location_id, limit=limit, after=after, before=before)

Get clan war rankings for a specific location

Get clan war rankings for a specific location

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
api_instance = pyroyale.LocationsApi(pyroyale.ApiClient(configuration))
location_id = 'location_id_example' # str | Identifier of the location to retrieve.
limit = 56 # int | Limit the number of items returned in the response.  (optional)
after = 56 # int | Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 56 # int | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

try:
    # Get clan war rankings for a specific location
    api_response = api_instance.get_clan_wars_ranking(location_id, limit=limit, after=after, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_clan_wars_ranking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| Identifier of the location to retrieve. | 
 **limit** | **int**| Limit the number of items returned in the response.  | [optional] 
 **after** | **int**| Return only items that occur after this marker. After marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **int**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**ClanWarsRankingList**](ClanWarsRankingList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location**
> Location get_location(location_id)

Get location information

Get information about specific location

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
api_instance = pyroyale.LocationsApi(pyroyale.ApiClient(configuration))
location_id = 'location_id_example' # str | Identifier of the location to retrieve.

try:
    # Get location information
    api_response = api_instance.get_location(location_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| Identifier of the location to retrieve. | 

### Return type

[**Location**](Location.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_locations**
> LocationList get_locations(limit=limit, after=after, before=before)

List locations

List all available locations

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
api_instance = pyroyale.LocationsApi(pyroyale.ApiClient(configuration))
limit = 56 # int | Limit the number of items returned in the response.  (optional)
after = 56 # int | Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 56 # int | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

try:
    # List locations
    api_response = api_instance.get_locations(limit=limit, after=after, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the number of items returned in the response.  | [optional] 
 **after** | **int**| Return only items that occur after this marker. After marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **int**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**LocationList**](LocationList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_ranking**
> PlayerRankingList get_player_ranking(location_id, limit=limit, after=after, before=before)

Get player rankings for a specific location

Get player rankings for a specific location

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
api_instance = pyroyale.LocationsApi(pyroyale.ApiClient(configuration))
location_id = 'location_id_example' # str | Identifier of the location to retrieve.
limit = 56 # int | Limit the number of items returned in the response.  (optional)
after = 56 # int | Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 56 # int | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

try:
    # Get player rankings for a specific location
    api_response = api_instance.get_player_ranking(location_id, limit=limit, after=after, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_player_ranking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| Identifier of the location to retrieve. | 
 **limit** | **int**| Limit the number of items returned in the response.  | [optional] 
 **after** | **int**| Return only items that occur after this marker. After marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **int**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**PlayerRankingList**](PlayerRankingList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

