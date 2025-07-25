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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.geo_json_object import GeoJsonObject
from openapi_client.models.named_resource_dto_facility_model import NamedResourceDTOFacilityModel
from openapi_client.models.named_resource_dto_group_model import NamedResourceDTOGroupModel
from openapi_client.models.named_resource_dto_organization_model import NamedResourceDTOOrganizationModel
from openapi_client.models.site_address_dto import SiteAddressDTO
from openapi_client.models.user_get_dto import UserGetDTO
from typing import Optional, Set
from typing_extensions import Self

class SiteGetDTO(BaseModel):
    """
    SiteGetDTO
    """ # noqa: E501
    uri: Optional[StrictStr] = None
    rdf_type: Optional[StrictStr] = None
    rdf_type_name: Optional[StrictStr] = None
    publisher: Optional[UserGetDTO] = None
    publication_date: Optional[datetime] = None
    last_updated_date: Optional[datetime] = None
    name: Optional[StrictStr] = None
    address: Optional[SiteAddressDTO] = None
    organizations: Optional[List[NamedResourceDTOOrganizationModel]] = None
    facilities: Optional[List[NamedResourceDTOFacilityModel]] = None
    groups: Optional[List[NamedResourceDTOGroupModel]] = None
    geometry: Optional[GeoJsonObject] = None
    description: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["uri", "rdf_type", "rdf_type_name", "publisher", "publication_date", "last_updated_date", "name", "address", "organizations", "facilities", "groups", "geometry", "description"]

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
        """Create an instance of SiteGetDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of publisher
        if self.publisher:
            _dict['publisher'] = self.publisher.to_dict()
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in organizations (list)
        _items = []
        if self.organizations:
            for _item_organizations in self.organizations:
                if _item_organizations:
                    _items.append(_item_organizations.to_dict())
            _dict['organizations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in facilities (list)
        _items = []
        if self.facilities:
            for _item_facilities in self.facilities:
                if _item_facilities:
                    _items.append(_item_facilities.to_dict())
            _dict['facilities'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in groups (list)
        _items = []
        if self.groups:
            for _item_groups in self.groups:
                if _item_groups:
                    _items.append(_item_groups.to_dict())
            _dict['groups'] = _items
        # override the default output from pydantic by calling `to_dict()` of geometry
        if self.geometry:
            _dict['geometry'] = self.geometry.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SiteGetDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uri": obj.get("uri"),
            "rdf_type": obj.get("rdf_type"),
            "rdf_type_name": obj.get("rdf_type_name"),
            "publisher": UserGetDTO.from_dict(obj["publisher"]) if obj.get("publisher") is not None else None,
            "publication_date": obj.get("publication_date"),
            "last_updated_date": obj.get("last_updated_date"),
            "name": obj.get("name"),
            "address": SiteAddressDTO.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "organizations": [NamedResourceDTOOrganizationModel.from_dict(_item) for _item in obj["organizations"]] if obj.get("organizations") is not None else None,
            "facilities": [NamedResourceDTOFacilityModel.from_dict(_item) for _item in obj["facilities"]] if obj.get("facilities") is not None else None,
            "groups": [NamedResourceDTOGroupModel.from_dict(_item) for _item in obj["groups"]] if obj.get("groups") is not None else None,
            "geometry": GeoJsonObject.from_dict(obj["geometry"]) if obj.get("geometry") is not None else None,
            "description": obj.get("description")
        })
        return _obj


