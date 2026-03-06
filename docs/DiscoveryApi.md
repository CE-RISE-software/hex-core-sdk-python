# ce_rise_hex_core_sdk.DiscoveryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_models**](DiscoveryApi.md#list_models) | **GET** /models | List available model versions


# **list_models**
> ModelsResponse list_models()

List available model versions

Returns model/version pairs currently loaded in the active registry index.

### Example


```python
import ce_rise_hex_core_sdk
from ce_rise_hex_core_sdk.models.models_response import ModelsResponse
from ce_rise_hex_core_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ce_rise_hex_core_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ce_rise_hex_core_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ce_rise_hex_core_sdk.DiscoveryApi(api_client)

    try:
        # List available model versions
        api_response = api_instance.list_models()
        print("The response of DiscoveryApi->list_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryApi->list_models: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ModelsResponse**](ModelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Registry models loaded successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

