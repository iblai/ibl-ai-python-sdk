# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.time_spent_by_users_in_course import TimeSpentByUsersInCourse

class TestTimeSpentByUsersInCourse(unittest.TestCase):
    """TimeSpentByUsersInCourse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeSpentByUsersInCourse:
        """Test TimeSpentByUsersInCourse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeSpentByUsersInCourse`
        """
        model = TimeSpentByUsersInCourse()
        if include_optional:
            return TimeSpentByUsersInCourse(
                data = [
                    iblai.models.time_spent_by_users_in_course_data.TimeSpentByUsersInCourseData(
                        username = '', 
                        full_name = '', 
                        email = '', 
                        assessments = 56, 
                        time_spent = '', )
                    ],
                pagination = iblai.models.pagination.Pagination(
                    total_items = 56, 
                    current_page = 56, 
                    per_page = 56, 
                    total_pages = 56, )
            )
        else:
            return TimeSpentByUsersInCourse(
                pagination = iblai.models.pagination.Pagination(
                    total_items = 56, 
                    current_page = 56, 
                    per_page = 56, 
                    total_pages = 56, ),
        )
        """

    def testTimeSpentByUsersInCourse(self):
        """Test TimeSpentByUsersInCourse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
