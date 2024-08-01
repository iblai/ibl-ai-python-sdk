# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.patched_slack_config import PatchedSlackConfig

class TestPatchedSlackConfig(unittest.TestCase):
    """PatchedSlackConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedSlackConfig:
        """Test PatchedSlackConfig
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedSlackConfig`
        """
        model = PatchedSlackConfig()
        if include_optional:
            return PatchedSlackConfig(
                id = 56,
                user = 0,
                slack_team_domain = '',
                slack_username = '',
                date_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return PatchedSlackConfig(
        )
        """

    def testPatchedSlackConfig(self):
        """Test PatchedSlackConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()