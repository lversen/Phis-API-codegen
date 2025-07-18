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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.graph_config_dto import GraphConfigDTO
from typing import Optional, Set
from typing_extensions import Self

class DashboardConfigDTO(BaseModel):
    """
    DashboardConfigDTO
    """ # noqa: E501
    show_metrics: Optional[StrictBool] = Field(default=None, alias="showMetrics")
    graph1: Optional[GraphConfigDTO] = None
    graph2: Optional[GraphConfigDTO] = None
    graph3: Optional[GraphConfigDTO] = None
    __properties: ClassVar[List[str]] = ["showMetrics", "graph1", "graph2", "graph3"]

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
        """Create an instance of DashboardConfigDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of graph1
        if self.graph1:
            _dict['graph1'] = self.graph1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of graph2
        if self.graph2:
            _dict['graph2'] = self.graph2.to_dict()
        # override the default output from pydantic by calling `to_dict()` of graph3
        if self.graph3:
            _dict['graph3'] = self.graph3.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DashboardConfigDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "showMetrics": obj.get("showMetrics"),
            "graph1": GraphConfigDTO.from_dict(obj["graph1"]) if obj.get("graph1") is not None else None,
            "graph2": GraphConfigDTO.from_dict(obj["graph2"]) if obj.get("graph2") is not None else None,
            "graph3": GraphConfigDTO.from_dict(obj["graph3"]) if obj.get("graph3") is not None else None
        })
        return _obj


