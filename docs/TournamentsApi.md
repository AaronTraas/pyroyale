# pyroyale.TournamentsApi

All URIs are relative to *https://api.clashroyale.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_global_tournaments**](TournamentsApi.md#get_global_tournaments) | **GET** /globaltournaments | List global tournaments
[**get_tournament**](TournamentsApi.md#get_tournament) | **GET** /tournaments/{tournamentTag} | Get tournament information
[**search_tournaments**](TournamentsApi.md#search_tournaments) | **GET** /tournaments | Search tournaments

# **get_global_tournaments**
> TournamentSearchResult get_global_tournaments()

List global tournaments

List all available global tournaments.

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
api_instance = pyroyale.TournamentsApi(pyroyale.ApiClient(configuration))

try:
    # List global tournaments
    api_response = api_instance.get_global_tournaments()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TournamentsApi->get_global_tournaments: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TournamentSearchResult**](TournamentSearchResult.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tournament**
> Tournament get_tournament(tournament_tag)

Get tournament information

Get information about a single tournament by a tournament tag. 

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
api_instance = pyroyale.TournamentsApi(pyroyale.ApiClient(configuration))
tournament_tag = 'tournament_tag_example' # str | Tag of the tournament to retrieve. 

try:
    # Get tournament information
    api_response = api_instance.get_tournament(tournament_tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TournamentsApi->get_tournament: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tournament_tag** | **str**| Tag of the tournament to retrieve.  | 

### Return type

[**Tournament**](Tournament.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_tournaments**
> TournamentSearchResult search_tournaments(name=name, limit=limit, after=after, before=before)

Search tournaments

Search all tournaments by name. It is not possible to specify ordering for results so clients should not rely on any specific ordering as that may change in the future releases of the API. 

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
api_instance = pyroyale.TournamentsApi(pyroyale.ApiClient(configuration))
name = 'name_example' # str | Search tournaments by name.  (optional)
limit = 56 # int | Limit the number of items returned in the response.  (optional)
after = 56 # int | Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 56 # int | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

try:
    # Search tournaments
    api_response = api_instance.search_tournaments(name=name, limit=limit, after=after, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TournamentsApi->search_tournaments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Search tournaments by name.  | [optional] 
 **limit** | **int**| Limit the number of items returned in the response.  | [optional] 
 **after** | **int**| Return only items that occur after this marker. After marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **int**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**TournamentSearchResult**](TournamentSearchResult.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

