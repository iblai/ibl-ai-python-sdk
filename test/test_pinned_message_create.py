# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.pinned_message_create import PinnedMessageCreate

class TestPinnedMessageCreate(unittest.TestCase):
    """PinnedMessageCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PinnedMessageCreate:
        """Test PinnedMessageCreate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PinnedMessageCreate`
        """
        model = PinnedMessageCreate()
        if include_optional:
            return PinnedMessageCreate(
                id = 56,
                platform = '',
                username = '',
                session_id = ''
            )
        else:
            return PinnedMessageCreate(
                id = 56,
                platform = '',
                username = '',
                session_id = '',
        )
        """

    def testPinnedMessageCreate(self):
        """Test PinnedMessageCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()