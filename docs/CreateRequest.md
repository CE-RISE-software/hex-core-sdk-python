# CreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **Dict[str, object]** | Payload to validate and persist as a new record. | 

## Example

```python
from ce_rise_hex_core_sdk.models.create_request import CreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRequest from a JSON string
create_request_instance = CreateRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRequest.to_json())

# convert the object into a dict
create_request_dict = create_request_instance.to_dict()
# create an instance of CreateRequest from a dict
create_request_from_dict = CreateRequest.from_dict(create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


