# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.report_data import ReportData

class TestReportData(unittest.TestCase):
    """ReportData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReportData:
        """Test ReportData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReportData`
        """
        model = ReportData()
        if include_optional:
            return ReportData(
                display_name = '',
                description = '',
                report_name = '',
                icon = '',
                extra_query_params = [
                    null
                    ],
                result_columns = [
                    null
                    ],
                status = iblai.models.report_status.ReportStatus(
                    report_id = '', 
                    report_name = '', 
                    state = null, 
                    started_on = '', 
                    owner = '', 
                    expires = '', 
                    url = '', )
            )
        else:
            return ReportData(
        )
        """

    def testReportData(self):
        """Test ReportData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()