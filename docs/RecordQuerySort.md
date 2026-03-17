# RecordQuerySort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Sortable field path such as &#x60;created_at&#x60; or &#x60;payload.record_scope&#x60;. | 
**direction** | **str** | Sort direction. | 

## Example

```python
from ce_rise_hex_core_sdk.models.record_query_sort import RecordQuerySort

# TODO update the JSON string below
json = "{}"
# create an instance of RecordQuerySort from a JSON string
record_query_sort_instance = RecordQuerySort.from_json(json)
# print the JSON string representation of the object
print(RecordQuerySort.to_json())

# convert the object into a dict
record_query_sort_dict = record_query_sort_instance.to_dict()
# create an instance of RecordQuerySort from a dict
record_query_sort_from_dict = RecordQuerySort.from_dict(record_query_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


