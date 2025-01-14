# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.course_grading_detail_data import CourseGradingDetailData

class TestCourseGradingDetailData(unittest.TestCase):
    """CourseGradingDetailData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CourseGradingDetailData:
        """Test CourseGradingDetailData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CourseGradingDetailData`
        """
        model = CourseGradingDetailData()
        if include_optional:
            return CourseGradingDetailData(
                display_name = '',
                id = '',
                subsections = [
                    iblai.models.course_grade_detail_sub_section.CourseGradeDetailSubSection(
                        display_name = '', 
                        id = '', 
                        attempts = '', 
                        average = '', 
                        problems = [
                            iblai.models.course_grade_detail_block.CourseGradeDetailBlock(
                                display_name = '', 
                                id = '', 
                                attempts = '', 
                                average = '', )
                            ], )
                    ]
            )
        else:
            return CourseGradingDetailData(
                display_name = '',
                id = '',
        )
        """

    def testCourseGradingDetailData(self):
        """Test CourseGradingDetailData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
