# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.math_question_cognitive_skills import MathQuestionCognitiveSkills

class TestMathQuestionCognitiveSkills(unittest.TestCase):
    """MathQuestionCognitiveSkills unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MathQuestionCognitiveSkills:
        """Test MathQuestionCognitiveSkills
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MathQuestionCognitiveSkills`
        """
        model = MathQuestionCognitiveSkills()
        if include_optional:
            return MathQuestionCognitiveSkills(
            )
        else:
            return MathQuestionCognitiveSkills(
        )
        """

    def testMathQuestionCognitiveSkills(self):
        """Test MathQuestionCognitiveSkills"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
