# PositionCreationDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**point** | [**Point**](Point.md) |  | [optional] 
**x** | **str** |  | [optional] 
**y** | **str** |  | [optional] 
**z** | **str** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.position_creation_dto import PositionCreationDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PositionCreationDTO from a JSON string
position_creation_dto_instance = PositionCreationDTO.from_json(json)
# print the JSON string representation of the object
print(PositionCreationDTO.to_json())

# convert the object into a dict
position_creation_dto_dict = position_creation_dto_instance.to_dict()
# create an instance of PositionCreationDTO from a dict
position_creation_dto_from_dict = PositionCreationDTO.from_dict(position_creation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


