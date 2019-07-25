# pyroyale.CardsApi

All URIs are relative to *https://api.clashroyale.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cards**](CardsApi.md#get_cards) | **GET** /cards | Get list of available cards


# **get_cards**
> CardList get_cards()

Get list of available cards

Get list of all available cards. 

### Example

* Api Key Authentication (JWT):
```python
from __future__ import print_function
import time
import pyroyale
from pyroyale.rest import ApiException
from pprint import pprint
configuration = pyroyale.Configuration()
# Configure API key authorization: JWT
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to https://api.clashroyale.com/v1
configuration.host = "https://api.clashroyale.com/v1"
# Create an instance of the API class
api_instance = pyroyale.CardsApi(pyroyale.ApiClient(configuration))

try:
    # Get list of available cards
    api_response = api_instance.get_cards()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardsApi->get_cards: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CardList**](CardList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Client provided incorrect parameters for the request. |  -  |
**403** | Access denied, either because of missing/incorrect credentials or used API token does not grant access to the requested resource.  |  -  |
**404** | Resource was not found. |  -  |
**429** | Request was throttled, because amount of requests was above the threshold defined for the used API token.  |  -  |
**500** | Unknown error happened when handling the request.  |  -  |
**503** | Service is temprorarily unavailable because of maintenance.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

