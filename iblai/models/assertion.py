# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from iblai.models.acceptance_enum import AcceptanceEnum
from typing import Optional, Set
from typing_extensions import Self

class Assertion(BaseModel):
    """
    Assertion
    """ # noqa: E501
    entity_id: StrictStr = Field(alias="entityId")
    issued_on: StrictStr = Field(alias="issuedOn")
    credential_details: Dict[str, StrictStr] = Field(alias="credentialDetails")
    recipient: Dict[str, StrictStr]
    metadata: Optional[Any] = None
    course: Dict[str, StrictStr]
    program: Dict[str, StrictStr]
    narrative: Optional[StrictStr] = None
    revoked: Optional[StrictBool] = None
    revocation_reason: StrictStr = Field(alias="revocationReason")
    acceptance: Optional[AcceptanceEnum] = None
    expires: StrictStr
    __properties: ClassVar[List[str]] = ["entityId", "issuedOn", "credentialDetails", "recipient", "metadata", "course", "program", "narrative", "revoked", "revocationReason", "acceptance", "expires"]

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
        """Create an instance of Assertion from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "credential_details",
            "recipient",
            "course",
            "program",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if narrative (nullable) is None
        # and model_fields_set contains the field
        if self.narrative is None and "narrative" in self.model_fields_set:
            _dict['narrative'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Assertion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "entityId": obj.get("entityId"),
            "issuedOn": obj.get("issuedOn"),
            "credentialDetails": obj.get("credentialDetails"),
            "recipient": obj.get("recipient"),
            "metadata": obj.get("metadata"),
            "course": obj.get("course"),
            "program": obj.get("program"),
            "narrative": obj.get("narrative"),
            "revoked": obj.get("revoked"),
            "revocationReason": obj.get("revocationReason"),
            "acceptance": obj.get("acceptance"),
            "expires": obj.get("expires")
        })
        return _obj

