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

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.rdf_object_relation_dto import RDFObjectRelationDTO
from openapi_client.models.user_get_dto import UserGetDTO
from typing import Optional, Set
from typing_extensions import Self

class DeviceCreationDTO(BaseModel):
    """
    DeviceCreationDTO
    """ # noqa: E501
    uri: Optional[StrictStr] = Field(default=None, description="Device URI")
    rdf_type: StrictStr = Field(description="rdfType URI")
    name: StrictStr = Field(description="Device name")
    brand: Optional[StrictStr] = None
    constructor_model: Optional[StrictStr] = None
    serial_number: Optional[StrictStr] = None
    person_in_charge: Optional[StrictStr] = Field(default=None, description="Person in charge")
    start_up: Optional[date] = None
    removal: Optional[date] = None
    relations: Optional[List[RDFObjectRelationDTO]] = None
    description: Optional[StrictStr] = None
    metadata: Optional[Dict[str, StrictStr]] = None
    publisher: Optional[UserGetDTO] = None
    publication_date: Optional[datetime] = None
    last_updated_date: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["uri", "rdf_type", "name", "brand", "constructor_model", "serial_number", "person_in_charge", "start_up", "removal", "relations", "description", "metadata", "publisher", "publication_date", "last_updated_date"]

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
        """Create an instance of DeviceCreationDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in relations (list)
        _items = []
        if self.relations:
            for _item_relations in self.relations:
                if _item_relations:
                    _items.append(_item_relations.to_dict())
            _dict['relations'] = _items
        # override the default output from pydantic by calling `to_dict()` of publisher
        if self.publisher:
            _dict['publisher'] = self.publisher.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceCreationDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uri": obj.get("uri"),
            "rdf_type": obj.get("rdf_type"),
            "name": obj.get("name"),
            "brand": obj.get("brand"),
            "constructor_model": obj.get("constructor_model"),
            "serial_number": obj.get("serial_number"),
            "person_in_charge": obj.get("person_in_charge"),
            "start_up": obj.get("start_up"),
            "removal": obj.get("removal"),
            "relations": [RDFObjectRelationDTO.from_dict(_item) for _item in obj["relations"]] if obj.get("relations") is not None else None,
            "description": obj.get("description"),
            "metadata": obj.get("metadata"),
            "publisher": UserGetDTO.from_dict(obj["publisher"]) if obj.get("publisher") is not None else None,
            "publication_date": obj.get("publication_date"),
            "last_updated_date": obj.get("last_updated_date")
        })
        return _obj


