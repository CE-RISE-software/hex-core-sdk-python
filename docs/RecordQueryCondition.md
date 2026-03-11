# RecordQueryCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field path such as &#x60;id&#x60; or &#x60;payload.record_scope&#x60;. | 
**op** | **str** | Comparison operator. | 
**value** | **object** | Operand value. For &#x60;in&#x60; this must be an array. For &#x60;exists&#x60; this should be boolean. | 

## Example

```python
from ce_rise_hex_core_sdk.models.record_query_condition import RecordQueryCondition

# TODO update the JSON string below
json = "{}"
# create an instance of RecordQueryCondition from a JSON string
record_query_condition_instance = RecordQueryCondition.from_json(json)
# print the JSON string representation of the object
print(RecordQueryCondition.to_json())

# convert the object into a dict
record_query_condition_dict = record_query_condition_instance.to_dict()
# create an instance of RecordQueryCondition from a dict
record_query_condition_from_dict = RecordQueryCondition.from_dict(record_query_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


