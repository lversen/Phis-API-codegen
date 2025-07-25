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

from datetime import date
from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ExperimentGetListDTO(BaseModel):
    """
    ExperimentGetListDTO
    """ # noqa: E501
    uri: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    description: Optional[StrictStr] = None
    objective: Optional[StrictStr] = None
    species: Optional[List[StrictStr]] = None
    is_public: Optional[StrictBool] = None
    facilities: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["uri", "name", "start_date", "end_date", "description", "objective", "species", "is_public", "facilities"]

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
        """Create an instance of ExperimentGetListDTO from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExperimentGetListDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uri": obj.get("uri"),
            "name": obj.get("name"),
            "start_date": obj.get("start_date"),
            "end_date": obj.get("end_date"),
            "description": obj.get("description"),
            "objective": obj.get("objective"),
            "species": obj.get("species"),
            "is_public": obj.get("is_public"),
            "facilities": obj.get("facilities")
        })
        return _obj


