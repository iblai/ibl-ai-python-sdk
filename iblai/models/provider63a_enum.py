# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class Provider63aEnum(str, Enum):
    """
    * `openai` - Openai
    """

    """
    allowed enum values
    """
    OPENAI = 'openai'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Provider63aEnum from a JSON string"""
        return cls(json.loads(json_str))


