# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.reported_skill import ReportedSkill

class TestReportedSkill(unittest.TestCase):
    """ReportedSkill unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReportedSkill:
        """Test ReportedSkill
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReportedSkill`
        """
        model = ReportedSkill()
        if include_optional:
            return ReportedSkill(
                skills = [
                    iblai.models.skill.Skill(
                        id = 56, 
                        name = '', )
                    ]
            )
        else:
            return ReportedSkill(
                skills = [
                    iblai.models.skill.Skill(
                        id = 56, 
                        name = '', )
                    ],
        )
        """

    def testReportedSkill(self):
        """Test ReportedSkill"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
