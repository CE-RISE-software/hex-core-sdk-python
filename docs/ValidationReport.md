# ValidationReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passed** | **bool** | True when no blocking validation issues were found. | 
**results** | [**List[ValidationResult]**](ValidationResult.md) |  | 

## Example

```python
from ce_rise_hex_core_sdk.models.validation_report import ValidationReport

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationReport from a JSON string
validation_report_instance = ValidationReport.from_json(json)
# print the JSON string representation of the object
print(ValidationReport.to_json())

# convert the object into a dict
validation_report_dict = validation_report_instance.to_dict()
# create an instance of ValidationReport from a dict
validation_report_from_dict = ValidationReport.from_dict(validation_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


