# ModelCountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models_count** | **int** | Number of models currently indexed by the registry. | 

## Example

```python
from ce_rise_hex_core_sdk.models.model_count_response import ModelCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCountResponse from a JSON string
model_count_response_instance = ModelCountResponse.from_json(json)
# print the JSON string representation of the object
print(ModelCountResponse.to_json())

# convert the object into a dict
model_count_response_dict = model_count_response_instance.to_dict()
# create an instance of ModelCountResponse from a dict
model_count_response_from_dict = ModelCountResponse.from_dict(model_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


