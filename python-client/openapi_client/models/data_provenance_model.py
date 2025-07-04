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
from openapi_client.models.prov_entity_model import ProvEntityModel
from typing import Optional, Set
from typing_extensions import Self

class DataProvenanceModel(BaseModel):
    """
    DataProvenanceModel
    """ # noqa: E501
    uri: StrictStr = Field(description="provenance uri")
    prov_used: Optional[List[ProvEntityModel]] = Field(default=None, description="list of inputs of the process described in the provenance")
    prov_was_associated_with: Optional[List[ProvEntityModel]] = Field(default=None, description="allow an activity to be linked to an agent")
    settings: Optional[Dict[str, Dict[str, Any]]] = Field(default=None, description="a key-value system to store specific information")
    experiments: Optional[List[StrictStr]] = Field(default=None, description="experiments uris on which the data has been produced")
    __properties: ClassVar[List[str]] = ["uri", "prov_used", "prov_was_associated_with", "settings", "experiments"]

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
        """Create an instance of DataProvenanceModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in prov_used (list)
        _items = []
        if self.prov_used:
            for _item_prov_used in self.prov_used:
                if _item_prov_used:
                    _items.append(_item_prov_used.to_dict())
            _dict['prov_used'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in prov_was_associated_with (list)
        _items = []
        if self.prov_was_associated_with:
            for _item_prov_was_associated_with in self.prov_was_associated_with:
                if _item_prov_was_associated_with:
                    _items.append(_item_prov_was_associated_with.to_dict())
            _dict['prov_was_associated_with'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataProvenanceModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uri": obj.get("uri"),
            "prov_used": [ProvEntityModel.from_dict(_item) for _item in obj["prov_used"]] if obj.get("prov_used") is not None else None,
            "prov_was_associated_with": [ProvEntityModel.from_dict(_item) for _item in obj["prov_was_associated_with"]] if obj.get("prov_was_associated_with") is not None else None,
            "settings": obj.get("settings"),
            "experiments": obj.get("experiments")
        })
        return _obj


