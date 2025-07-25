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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AccountGetDTO(BaseModel):
    """
    AccountGetDTO
    """ # noqa: E501
    uri: Optional[StrictStr] = Field(default=None, description="Account URI")
    email: Optional[StrictStr] = Field(default=None, description="Account email")
    admin: Optional[StrictBool] = Field(default=None, description="Account admin flag")
    language: Optional[StrictStr] = Field(default=None, description="Account language")
    enable: Optional[StrictBool] = Field(default=None, description="Account is enable")
    favorites: Optional[List[StrictStr]] = Field(default=None, description="Favorites URI")
    linked_person: Optional[StrictStr] = Field(default=None, description="URI of the Person linked to this account")
    person_first_name: Optional[StrictStr] = Field(default=None, description="first name of the linked person")
    person_last_name: Optional[StrictStr] = Field(default=None, description="last name of the linked person")
    __properties: ClassVar[List[str]] = ["uri", "email", "admin", "language", "enable", "favorites", "linked_person", "person_first_name", "person_last_name"]

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
        """Create an instance of AccountGetDTO from a JSON string"""
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
        """Create an instance of AccountGetDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uri": obj.get("uri"),
            "email": obj.get("email"),
            "admin": obj.get("admin"),
            "language": obj.get("language"),
            "enable": obj.get("enable"),
            "favorites": obj.get("favorites"),
            "linked_person": obj.get("linked_person"),
            "person_first_name": obj.get("person_first_name"),
            "person_last_name": obj.get("person_last_name")
        })
        return _obj


