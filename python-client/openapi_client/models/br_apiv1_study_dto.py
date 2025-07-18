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

class BrAPIv1StudyDTO(BaseModel):
    """
    BrAPIv1StudyDTO
    """ # noqa: E501
    active: Optional[StrictStr] = None
    additional_info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="additionalInfo")
    common_crop_name: Optional[StrictStr] = Field(default=None, alias="commonCropName")
    documentation_url: Optional[StrictStr] = Field(default=None, alias="documentationURL")
    end_date: Optional[StrictStr] = Field(default=None, alias="endDate")
    location_db_id: Optional[StrictStr] = Field(default=None, alias="locationDbId")
    location_name: Optional[StrictStr] = Field(default=None, alias="locationName")
    program_db_id: Optional[StrictStr] = Field(default=None, alias="programDbId")
    program_name: Optional[StrictStr] = Field(default=None, alias="programName")
    start_date: Optional[StrictStr] = Field(default=None, alias="startDate")
    study_db_id: Optional[StrictStr] = Field(default=None, alias="studyDbId")
    study_name: Optional[StrictStr] = Field(default=None, alias="studyName")
    study_type_db_id: Optional[StrictStr] = Field(default=None, alias="studyTypeDbId")
    study_type_name: Optional[StrictStr] = Field(default=None, alias="studyTypeName")
    trial_db_id: Optional[StrictStr] = Field(default=None, alias="trialDbId")
    trial_name: Optional[StrictStr] = Field(default=None, alias="trialName")
    seasons: Optional[List[BrAPIv1SeasonDTO]] = None
    __properties: ClassVar[List[str]] = ["active", "additionalInfo", "commonCropName", "documentationURL", "endDate", "locationDbId", "locationName", "programDbId", "programName", "startDate", "studyDbId", "studyName", "studyTypeDbId", "studyTypeName", "trialDbId", "trialName", "seasons"]

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
        """Create an instance of BrAPIv1StudyDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in seasons (list)
        _items = []
        if self.seasons:
            for _item_seasons in self.seasons:
                if _item_seasons:
                    _items.append(_item_seasons.to_dict())
            _dict['seasons'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BrAPIv1StudyDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "active": obj.get("active"),
            "additionalInfo": obj.get("additionalInfo"),
            "commonCropName": obj.get("commonCropName"),
            "documentationURL": obj.get("documentationURL"),
            "endDate": obj.get("endDate"),
            "locationDbId": obj.get("locationDbId"),
            "locationName": obj.get("locationName"),
            "programDbId": obj.get("programDbId"),
            "programName": obj.get("programName"),
            "startDate": obj.get("startDate"),
            "studyDbId": obj.get("studyDbId"),
            "studyName": obj.get("studyName"),
            "studyTypeDbId": obj.get("studyTypeDbId"),
            "studyTypeName": obj.get("studyTypeName"),
            "trialDbId": obj.get("trialDbId"),
            "trialName": obj.get("trialName"),
            "seasons": [BrAPIv1SeasonDTO.from_dict(_item) for _item in obj["seasons"]] if obj.get("seasons") is not None else None
        })
        return _obj


