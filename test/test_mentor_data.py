# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.mentor_data import MentorData

class TestMentorData(unittest.TestCase):
    """MentorData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MentorData:
        """Test MentorData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MentorData`
        """
        model = MentorData()
        if include_optional:
            return MentorData(
                mentor = '',
                total_cost = 1.337,
                total_latency = 1.337,
                mentor_traces = [
                    iblai.models.mentor_trace.MentorTrace(
                        session_id = '', 
                        cost = 1.337, 
                        latency = 1.337, 
                        username = '', )
                    ]
            )
        else:
            return MentorData(
                mentor = '',
                total_cost = 1.337,
                total_latency = 1.337,
                mentor_traces = [
                    iblai.models.mentor_trace.MentorTrace(
                        session_id = '', 
                        cost = 1.337, 
                        latency = 1.337, 
                        username = '', )
                    ],
        )
        """

    def testMentorData(self):
        """Test MentorData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
