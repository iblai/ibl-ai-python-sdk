# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.score import Score

class TestScore(unittest.TestCase):
    """Score unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Score:
        """Test Score
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Score`
        """
        model = Score()
        if include_optional:
            return Score(
                id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                value = 1.337,
                comment = '',
                trace_id = '',
                observation_id = '',
                trace = None
            )
        else:
            return Score(
                id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                value = 1.337,
                comment = '',
                trace_id = '',
                observation_id = '',
        )
        """

    def testScore(self):
        """Test Score"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
