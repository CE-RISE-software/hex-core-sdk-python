# RecordQueryFilter

Canonical backend query dialect shared across record store adapters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**where** | [**List[RecordQueryCondition]**](RecordQueryCondition.md) | AND-only list of query predicates. | 
**sort** | [**List[RecordQuerySort]**](RecordQuerySort.md) | Optional list of sort directives applied in order. | [optional] 
**limit** | **int** | Maximum number of records to return. | [optional] 
**offset** | **int** | Zero-based row offset for pagination. | [optional] 

## Example

```python
from ce_rise_hex_core_sdk.models.record_query_filter import RecordQueryFilter

# TODO update the JSON string below
json = "{}"
# create an instance of RecordQueryFilter from a JSON string
record_query_filter_instance = RecordQueryFilter.from_json(json)
# print the JSON string representation of the object
print(RecordQueryFilter.to_json())

# convert the object into a dict
record_query_filter_dict = record_query_filter_instance.to_dict()
# create an instance of RecordQueryFilter from a dict
record_query_filter_from_dict = RecordQueryFilter.from_dict(record_query_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


