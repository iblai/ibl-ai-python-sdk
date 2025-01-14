# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.paginated_periodic_agent_log_list import PaginatedPeriodicAgentLogList

class TestPaginatedPeriodicAgentLogList(unittest.TestCase):
    """PaginatedPeriodicAgentLogList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedPeriodicAgentLogList:
        """Test PaginatedPeriodicAgentLogList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedPeriodicAgentLogList`
        """
        model = PaginatedPeriodicAgentLogList()
        if include_optional:
            return PaginatedPeriodicAgentLogList(
                count = 123,
                next = 'http://api.example.org/accounts/?page=4',
                previous = 'http://api.example.org/accounts/?page=2',
                results = [
                    iblai.models.periodic_agent_log.PeriodicAgentLog(
                        id = 56, 
                        content = '', 
                        status = 'success', 
                        start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        periodic_agent = 56, )
                    ]
            )
        else:
            return PaginatedPeriodicAgentLogList(
        )
        """

    def testPaginatedPeriodicAgentLogList(self):
        """Test PaginatedPeriodicAgentLogList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
