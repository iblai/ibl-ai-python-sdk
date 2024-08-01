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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class TopicDetail(BaseModel):
    """
    TopicDetail
    """ # noqa: E501
    id: StrictInt
    total_topics: StrictInt
    number_of_messages: StrictInt
    number_of_conversations: StrictInt
    user_sentiment: StrictStr
    user_ratings: StrictStr
    name: Annotated[str, Field(strict=True, max_length=255)]
    metadata: Optional[Any] = None
    created_at: datetime
    platform: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["id", "total_topics", "number_of_messages", "number_of_conversations", "user_sentiment", "user_ratings", "name", "metadata", "created_at", "platform"]

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
        """Create an instance of TopicDetail from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "id",
            "created_at",
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

        # set to None if platform (nullable) is None
        # and model_fields_set contains the field
        if self.platform is None and "platform" in self.model_fields_set:
            _dict['platform'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TopicDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "total_topics": obj.get("total_topics"),
            "number_of_messages": obj.get("number_of_messages"),
            "number_of_conversations": obj.get("number_of_conversations"),
            "user_sentiment": obj.get("user_sentiment"),
            "user_ratings": obj.get("user_ratings"),
            "name": obj.get("name"),
            "metadata": obj.get("metadata"),
            "created_at": obj.get("created_at"),
            "platform": obj.get("platform")
        })
        return _obj


