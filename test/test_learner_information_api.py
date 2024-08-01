# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.learner_information_api import LearnerInformationAPI

class TestLearnerInformationAPI(unittest.TestCase):
    """LearnerInformationAPI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LearnerInformationAPI:
        """Test LearnerInformationAPI
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LearnerInformationAPI`
        """
        model = LearnerInformationAPI()
        if include_optional:
            return LearnerInformationAPI(
                data = iblai.models.learner_information_api_data.LearnerInformationAPIData(
                    username = '', 
                    name = '', 
                    email = '', 
                    date_joined = '', 
                    last_activity = '', 
                    total_assessments = 56, 
                    total_time_spent = 56, 
                    total_videos = 56, 
                    course_completions = 56, 
                    time_spent_overtime = {
                        'key' : null
                        }, 
                    continent = '', 
                    continent_code = '', 
                    country = '', 
                    country_code = '', 
                    region = '', 
                    region_code = '', 
                    location = '', 
                    city = '', 
                    browser = '', 
                    operating_system = '', 
                    resolution = '', )
            )
        else:
            return LearnerInformationAPI(
                data = iblai.models.learner_information_api_data.LearnerInformationAPIData(
                    username = '', 
                    name = '', 
                    email = '', 
                    date_joined = '', 
                    last_activity = '', 
                    total_assessments = 56, 
                    total_time_spent = 56, 
                    total_videos = 56, 
                    course_completions = 56, 
                    time_spent_overtime = {
                        'key' : null
                        }, 
                    continent = '', 
                    continent_code = '', 
                    country = '', 
                    country_code = '', 
                    region = '', 
                    region_code = '', 
                    location = '', 
                    city = '', 
                    browser = '', 
                    operating_system = '', 
                    resolution = '', ),
        )
        """

    def testLearnerInformationAPI(self):
        """Test LearnerInformationAPI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()