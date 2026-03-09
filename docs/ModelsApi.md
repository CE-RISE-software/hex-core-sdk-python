# ce_rise_hex_core_sdk.ModelsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_record**](ModelsApi.md#create_record) | **POST** /models/{model}/versions/{version}:create | Validate and create a record
[**query_records**](ModelsApi.md#query_records) | **POST** /models/{model}/versions/{version}:query | Query records for a model version
[**validate_model_payload**](ModelsApi.md#validate_model_payload) | **POST** /models/{model}/versions/{version}:validate | Validate payload against model rules


# **create_record**
> Record create_record(model, version, idempotency_key, create_request)

Validate and create a record

Validates input payload and writes a new record through the configured record store adapter.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import ce_rise_hex_core_sdk
from ce_rise_hex_core_sdk.models.create_request import CreateRequest
from ce_rise_hex_core_sdk.models.record import Record
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
    api_instance = ce_rise_hex_core_sdk.ModelsApi(api_client)
    model = 'model_example' # str | Model identifier.
    version = 'version_example' # str | Model version.
    idempotency_key = 'idempotency_key_example' # str | Client-generated key used to deduplicate retries for side-effecting requests.
    create_request = ce_rise_hex_core_sdk.CreateRequest() # CreateRequest | 

    try:
        # Validate and create a record
        api_response = api_instance.create_record(model, version, idempotency_key, create_request)
        print("The response of ModelsApi->create_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->create_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| Model identifier. | 
 **version** | **str**| Model version. | 
 **idempotency_key** | **str**| Client-generated key used to deduplicate retries for side-effecting requests. | 
 **create_request** | [**CreateRequest**](CreateRequest.md)|  | 

### Return type

[**Record**](Record.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Record created (or idempotent replay returned existing result). |  -  |
**401** | Authentication required or invalid token. |  -  |
**409** | Idempotency conflict. |  -  |
**422** | Validation failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_records**
> QueryResponse query_records(model, version, query_request)

Query records for a model version

Applies a filter object and returns matching records provided by the record store adapter.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import ce_rise_hex_core_sdk
from ce_rise_hex_core_sdk.models.query_request import QueryRequest
from ce_rise_hex_core_sdk.models.query_response import QueryResponse
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
    api_instance = ce_rise_hex_core_sdk.ModelsApi(api_client)
    model = 'model_example' # str | Model identifier.
    version = 'version_example' # str | Model version.
    query_request = ce_rise_hex_core_sdk.QueryRequest() # QueryRequest | 

    try:
        # Query records for a model version
        api_response = api_instance.query_records(model, version, query_request)
        print("The response of ModelsApi->query_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->query_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| Model identifier. | 
 **version** | **str**| Model version. | 
 **query_request** | [**QueryRequest**](QueryRequest.md)|  | 

### Return type

[**QueryResponse**](QueryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Matching records returned. |  -  |
**401** | Authentication required or invalid token. |  -  |
**404** | Requested model/version is not present in registry. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_model_payload**
> ValidationReport validate_model_payload(model, version, validate_request)

Validate payload against model rules

Runs configured validators for the selected model/version and returns a merged validation report.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import ce_rise_hex_core_sdk
from ce_rise_hex_core_sdk.models.validate_request import ValidateRequest
from ce_rise_hex_core_sdk.models.validation_report import ValidationReport
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
    api_instance = ce_rise_hex_core_sdk.ModelsApi(api_client)
    model = 'model_example' # str | Model identifier, for example `re-indicators-specification`.
    version = 'version_example' # str | Model version string, for example `0.0.3`.
    validate_request = ce_rise_hex_core_sdk.ValidateRequest() # ValidateRequest | 

    try:
        # Validate payload against model rules
        api_response = api_instance.validate_model_payload(model, version, validate_request)
        print("The response of ModelsApi->validate_model_payload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->validate_model_payload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| Model identifier, for example &#x60;re-indicators-specification&#x60;. | 
 **version** | **str**| Model version string, for example &#x60;0.0.3&#x60;. | 
 **validate_request** | [**ValidateRequest**](ValidateRequest.md)|  | 

### Return type

[**ValidationReport**](ValidationReport.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Validation report returned. |  -  |
**401** | Authentication required or invalid token. |  -  |
**404** | Requested model/version is not present in registry. |  -  |
**422** | Payload is syntactically valid JSON but violates model constraints. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

