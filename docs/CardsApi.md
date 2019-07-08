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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

