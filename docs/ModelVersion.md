# ModelVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Model identifier. | 
**version** | **str** | Model version string. | 

## Example

```python
from ce_rise_hex_core_sdk.models.model_version import ModelVersion

# TODO update the JSON string below
json = "{}"
# create an instance of ModelVersion from a JSON string
model_version_instance = ModelVersion.from_json(json)
# print the JSON string representation of the object
print(ModelVersion.to_json())

# convert the object into a dict
model_version_dict = model_version_instance.to_dict()
# create an instance of ModelVersion from a dict
model_version_from_dict = ModelVersion.from_dict(model_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


