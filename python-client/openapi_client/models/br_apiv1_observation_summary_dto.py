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

class BrAPIv1ObservationSummaryDTO(BaseModel):
    """
    BrAPIv1ObservationSummaryDTO
    """ # noqa: E501
    collector: Optional[StrictStr] = None
    observation_db_id: Optional[StrictStr] = Field(default=None, alias="observationDbId")
    observation_time_stamp: Optional[StrictStr] = Field(default=None, alias="observationTimeStamp")
    observation_variable_db_id: Optional[StrictStr] = Field(default=None, alias="observationVariableDbId")
    observation_variable_name: Optional[StrictStr] = Field(default=None, alias="observationVariableName")
    season: Optional[BrAPIv1SeasonDTO] = None
    value: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["collector", "observationDbId", "observationTimeStamp", "observationVariableDbId", "observationVariableName", "season", "value"]

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
        """Create an instance of BrAPIv1ObservationSummaryDTO from a JSON string"""
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
        """Create an instance of BrAPIv1ObservationSummaryDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "collector": obj.get("collector"),
            "observationDbId": obj.get("observationDbId"),
            "observationTimeStamp": obj.get("observationTimeStamp"),
            "observationVariableDbId": obj.get("observationVariableDbId"),
            "observationVariableName": obj.get("observationVariableName"),
            "season": BrAPIv1SeasonDTO.from_dict(obj["season"]) if obj.get("season") is not None else None,
            "value": obj.get("value")
        })
        return _obj


