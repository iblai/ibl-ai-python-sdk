# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.course_completion_per_course_data import CourseCompletionPerCourseData

class TestCourseCompletionPerCourseData(unittest.TestCase):
    """CourseCompletionPerCourseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CourseCompletionPerCourseData:
        """Test CourseCompletionPerCourseData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CourseCompletionPerCourseData`
        """
        model = CourseCompletionPerCourseData()
        if include_optional:
            return CourseCompletionPerCourseData(
                course_id = '',
                name = '',
                enrollments = 56,
                completions = 56,
                average = 1.337
            )
        else:
            return CourseCompletionPerCourseData(
                course_id = '',
                name = '',
                enrollments = 56,
                completions = 56,
                average = 1.337,
        )
        """

    def testCourseCompletionPerCourseData(self):
        """Test CourseCompletionPerCourseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
