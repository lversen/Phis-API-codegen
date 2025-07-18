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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.order_by import OrderBy
from typing import Optional, Set
from typing_extensions import Self

class ScientificObjectExportDTO(BaseModel):
    """
    ScientificObjectExportDTO
    """ # noqa: E501
    included_uris: Optional[List[StrictStr]] = Field(default=None, alias="includedUris")
    page: Optional[StrictInt] = Field(default=None, description="Page number")
    lang: Optional[StrictStr] = None
    rdf_types: Optional[List[StrictStr]] = None
    order_by: Optional[List[OrderBy]] = Field(default=None, description="List of fields to sort as an array of fieldName=asc|desc")
    page_size: Optional[StrictInt] = Field(default=None, description="Page size")
    uris: Optional[List[StrictStr]] = None
    excluded_uris: Optional[List[StrictStr]] = None
    experiment: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    parent: Optional[StrictStr] = None
    germplasm: Optional[List[StrictStr]] = None
    factor_levels: Optional[List[StrictStr]] = None
    facility: Optional[StrictStr] = None
    existence_date: Optional[date] = None
    creation_date: Optional[date] = None
    __properties: ClassVar[List[str]] = ["includedUris", "page", "lang", "rdf_types", "order_by", "page_size", "uris", "excluded_uris", "experiment", "name", "parent", "germplasm", "factor_levels", "facility", "existence_date", "creation_date"]

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
        """Create an instance of ScientificObjectExportDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in order_by (list)
        _items = []
        if self.order_by:
            for _item_order_by in self.order_by:
                if _item_order_by:
                    _items.append(_item_order_by.to_dict())
            _dict['order_by'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScientificObjectExportDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "includedUris": obj.get("includedUris"),
            "page": obj.get("page"),
            "lang": obj.get("lang"),
            "rdf_types": obj.get("rdf_types"),
            "order_by": [OrderBy.from_dict(_item) for _item in obj["order_by"]] if obj.get("order_by") is not None else None,
            "page_size": obj.get("page_size"),
            "uris": obj.get("uris"),
            "excluded_uris": obj.get("excluded_uris"),
            "experiment": obj.get("experiment"),
            "name": obj.get("name"),
            "parent": obj.get("parent"),
            "germplasm": obj.get("germplasm"),
            "factor_levels": obj.get("factor_levels"),
            "facility": obj.get("facility"),
            "existence_date": obj.get("existence_date"),
            "creation_date": obj.get("creation_date")
        })
        return _obj


