# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.4.7-rdg
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.br_apiv1_season_dto import BrAPIv1SeasonDTO
from typing import Optional, Set
from typing_extensions import Self

class BrAPIv1ObservationDTO(BaseModel):
    """
    BrAPIv1ObservationDTO
    """ # noqa: E501
    germplasm_db_id: Optional[StrictStr] = Field(default=None, alias="germplasmDbId")
    germplasm_name: Optional[StrictStr] = Field(default=None, alias="germplasmName")
    observation_db_id: Optional[StrictStr] = Field(default=None, alias="observationDbId")
    observation_level: Optional[StrictStr] = Field(default=None, alias="observationLevel")
    observation_time_stamp: Optional[StrictStr] = Field(default=None, alias="observationTimeStamp")
    observation_unit_db_id: Optional[StrictStr] = Field(default=None, alias="observationUnitDbId")
    observation_unit_name: Optional[StrictStr] = Field(default=None, alias="observationUnitName")
    observation_variable_db_id: Optional[StrictStr] = Field(default=None, alias="observationVariableDbId")
    observation_variable_name: Optional[StrictStr] = Field(default=None, alias="observationVariableName")
    operator: Optional[StrictStr] = None
    season: Optional[BrAPIv1SeasonDTO] = None
    study_db_id: Optional[StrictStr] = Field(default=None, alias="studyDbId")
    uploaded_by: Optional[StrictStr] = Field(default=None, alias="uploadedBy")
    value: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["germplasmDbId", "germplasmName", "observationDbId", "observationLevel", "observationTimeStamp", "observationUnitDbId", "observationUnitName", "observationVariableDbId", "observationVariableName", "operator", "season", "studyDbId", "uploadedBy", "value"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of BrAPIv1ObservationDTO from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of season
        if self.season:
            _dict['season'] = self.season.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BrAPIv1ObservationDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "germplasmDbId": obj.get("germplasmDbId"),
            "germplasmName": obj.get("germplasmName"),
            "observationDbId": obj.get("observationDbId"),
            "observationLevel": obj.get("observationLevel"),
            "observationTimeStamp": obj.get("observationTimeStamp"),
            "observationUnitDbId": obj.get("observationUnitDbId"),
            "observationUnitName": obj.get("observationUnitName"),
            "observationVariableDbId": obj.get("observationVariableDbId"),
            "observationVariableName": obj.get("observationVariableName"),
            "operator": obj.get("operator"),
            "season": BrAPIv1SeasonDTO.from_dict(obj["season"]) if obj.get("season") is not None else None,
            "studyDbId": obj.get("studyDbId"),
            "uploadedBy": obj.get("uploadedBy"),
            "value": obj.get("value")
        })
        return _obj


