# ce_rise_hex_core_sdk.AdminApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health**](AdminApi.md#health) | **GET** /admin/health | Liveness probe
[**metrics**](AdminApi.md#metrics) | **GET** /admin/metrics | Prometheus metrics
[**ready**](AdminApi.md#ready) | **GET** /admin/ready | Readiness probe
[**status**](AdminApi.md#status) | **GET** /admin/status | Runtime status


# **health**
> HealthResponse health()

Liveness probe

Returns service process liveness.

### Example


```python
import ce_rise_hex_core_sdk
from ce_rise_hex_core_sdk.models.health_response import HealthResponse
from ce_rise_hex_core_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = ce_rise_hex_core_sdk.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with ce_rise_hex_core_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ce_rise_hex_core_sdk.AdminApi(api_client)

    try:
        # Liveness probe
        api_response = api_instance.health()
        print("The response of AdminApi->health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->health: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthResponse**](HealthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service is alive. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics**
> str metrics()

Prometheus metrics

Returns Prometheus exposition format when metrics are enabled.

### Example


```python
import ce_rise_hex_core_sdk
from ce_rise_hex_core_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = ce_rise_hex_core_sdk.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with ce_rise_hex_core_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ce_rise_hex_core_sdk.AdminApi(api_client)

    try:
        # Prometheus metrics
        api_response = api_instance.metrics()
        print("The response of AdminApi->metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->metrics: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metrics text returned. |  -  |
**404** | Metrics endpoint disabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ready**
> ReadyResponse ready()

Readiness probe

Returns readiness based on runtime adapter and registry state.

### Example


```python
import ce_rise_hex_core_sdk
from ce_rise_hex_core_sdk.models.ready_response import ReadyResponse
from ce_rise_hex_core_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = ce_rise_hex_core_sdk.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with ce_rise_hex_core_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ce_rise_hex_core_sdk.AdminApi(api_client)

    try:
        # Readiness probe
        api_response = api_instance.ready()
        print("The response of AdminApi->ready:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->ready: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ReadyResponse**](ReadyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service is ready to accept traffic. |  -  |
**503** | Service is not ready. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status**
> Dict[str, object] status()

Runtime status

Returns runtime status payload useful for operations dashboards.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import ce_rise_hex_core_sdk
from ce_rise_hex_core_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = ce_rise_hex_core_sdk.Configuration(
    host = "http://localhost:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = ce_rise_hex_core_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ce_rise_hex_core_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ce_rise_hex_core_sdk.AdminApi(api_client)

    try:
        # Runtime status
        api_response = api_instance.status()
        print("The response of AdminApi->status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status payload returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

