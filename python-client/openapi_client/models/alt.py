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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from openapi_client.models.anon_id import AnonId
from openapi_client.models.literal import Literal
from openapi_client.models.model import Model
from openapi_client.models.rdf_node import RDFNode
from typing import Optional, Set
from typing_extensions import Self

class Alt(BaseModel):
    """
    Alt
    """ # noqa: E501
    default: Optional[RDFNode] = None
    default_language: Optional[StrictStr] = Field(default=None, alias="defaultLanguage")
    default_resource: Optional[Resource] = Field(default=None, alias="defaultResource")
    default_literal: Optional[Literal] = Field(default=None, alias="defaultLiteral")
    default_boolean: Optional[StrictBool] = Field(default=None, alias="defaultBoolean")
    default_byte: Optional[Union[Annotated[bytes, Field(strict=True)], Annotated[str, Field(strict=True)]]] = Field(default=None, alias="defaultByte")
    default_short: Optional[StrictInt] = Field(default=None, alias="defaultShort")
    default_int: Optional[StrictInt] = Field(default=None, alias="defaultInt")
    default_long: Optional[StrictInt] = Field(default=None, alias="defaultLong")
    default_char: Optional[StrictStr] = Field(default=None, alias="defaultChar")
    default_float: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="defaultFloat")
    default_double: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="defaultDouble")
    default_string: Optional[StrictStr] = Field(default=None, alias="defaultString")
    default_alt: Optional[Alt] = Field(default=None, alias="defaultAlt")
    default_bag: Optional[Bag] = Field(default=None, alias="defaultBag")
    default_seq: Optional[Seq] = Field(default=None, alias="defaultSeq")
    alt: Optional[StrictBool] = None
    seq: Optional[StrictBool] = None
    bag: Optional[StrictBool] = None
    id: Optional[AnonId] = None
    uri: Optional[StrictStr] = None
    local_name: Optional[StrictStr] = Field(default=None, alias="localName")
    name_space: Optional[StrictStr] = Field(default=None, alias="nameSpace")
    stmt_term: Optional[Statement] = Field(default=None, alias="stmtTerm")
    resource: Optional[StrictBool] = None
    model: Optional[Model] = None
    literal: Optional[StrictBool] = None
    anon: Optional[StrictBool] = None
    uriresource: Optional[StrictBool] = None
    stmt_resource: Optional[StrictBool] = Field(default=None, alias="stmtResource")
    __properties: ClassVar[List[str]] = ["default", "defaultLanguage", "defaultResource", "defaultLiteral", "defaultBoolean", "defaultByte", "defaultShort", "defaultInt", "defaultLong", "defaultChar", "defaultFloat", "defaultDouble", "defaultString", "defaultAlt", "defaultBag", "defaultSeq", "alt", "seq", "bag", "id", "uri", "localName", "nameSpace", "stmtTerm", "resource", "model", "literal", "anon", "uriresource", "stmtResource"]

    @field_validator('default_byte')
    def default_byte_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$", value):
            raise ValueError(r"must validate the regular expression /^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/")
        return value

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
        """Create an instance of Alt from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of default
        if self.default:
            _dict['default'] = self.default.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default_resource
        if self.default_resource:
            _dict['defaultResource'] = self.default_resource.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default_literal
        if self.default_literal:
            _dict['defaultLiteral'] = self.default_literal.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default_alt
        if self.default_alt:
            _dict['defaultAlt'] = self.default_alt.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default_bag
        if self.default_bag:
            _dict['defaultBag'] = self.default_bag.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default_seq
        if self.default_seq:
            _dict['defaultSeq'] = self.default_seq.to_dict()
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of stmt_term
        if self.stmt_term:
            _dict['stmtTerm'] = self.stmt_term.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict['model'] = self.model.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Alt from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "default": RDFNode.from_dict(obj["default"]) if obj.get("default") is not None else None,
            "defaultLanguage": obj.get("defaultLanguage"),
            "defaultResource": Resource.from_dict(obj["defaultResource"]) if obj.get("defaultResource") is not None else None,
            "defaultLiteral": Literal.from_dict(obj["defaultLiteral"]) if obj.get("defaultLiteral") is not None else None,
            "defaultBoolean": obj.get("defaultBoolean"),
            "defaultByte": obj.get("defaultByte"),
            "defaultShort": obj.get("defaultShort"),
            "defaultInt": obj.get("defaultInt"),
            "defaultLong": obj.get("defaultLong"),
            "defaultChar": obj.get("defaultChar"),
            "defaultFloat": obj.get("defaultFloat"),
            "defaultDouble": obj.get("defaultDouble"),
            "defaultString": obj.get("defaultString"),
            "defaultAlt": Alt.from_dict(obj["defaultAlt"]) if obj.get("defaultAlt") is not None else None,
            "defaultBag": Bag.from_dict(obj["defaultBag"]) if obj.get("defaultBag") is not None else None,
            "defaultSeq": Seq.from_dict(obj["defaultSeq"]) if obj.get("defaultSeq") is not None else None,
            "alt": obj.get("alt"),
            "seq": obj.get("seq"),
            "bag": obj.get("bag"),
            "id": AnonId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "uri": obj.get("uri"),
            "localName": obj.get("localName"),
            "nameSpace": obj.get("nameSpace"),
            "stmtTerm": Statement.from_dict(obj["stmtTerm"]) if obj.get("stmtTerm") is not None else None,
            "resource": obj.get("resource"),
            "model": Model.from_dict(obj["model"]) if obj.get("model") is not None else None,
            "literal": obj.get("literal"),
            "anon": obj.get("anon"),
            "uriresource": obj.get("uriresource"),
            "stmtResource": obj.get("stmtResource")
        })
        return _obj

from openapi_client.models.bag import Bag
from openapi_client.models.resource import Resource
from openapi_client.models.seq import Seq
from openapi_client.models.statement import Statement
# TODO: Rewrite to not use raise_errors
Alt.model_rebuild(raise_errors=False)

