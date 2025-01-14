# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.patched_periodic_agent_create import PatchedPeriodicAgentCreate

class TestPatchedPeriodicAgentCreate(unittest.TestCase):
    """PatchedPeriodicAgentCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedPeriodicAgentCreate:
        """Test PatchedPeriodicAgentCreate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedPeriodicAgentCreate`
        """
        model = PatchedPeriodicAgentCreate()
        if include_optional:
            return PatchedPeriodicAgentCreate(
                id = 56,
                mentor = 56,
                title = '',
                username = '',
                description = '',
                prompt = '',
                task = iblai.models.periodic_task.PeriodicTask(
                    id = 56, 
                    name = '', 
                    crontab = iblai.models.crontab_schedule.CrontabSchedule(
                        minute = '', 
                        hour = '', 
                        day_of_week = '', 
                        day_of_month = '', 
                        month_of_year = '', ), 
                    one_off = True, 
                    start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    enabled = True, ),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                enabled = True,
                one_off = '',
                platform_key = '',
                pathway = '',
                callback_url = '',
                callback_secret = '',
                parent_session_id = '',
                parent_mentor_id = 56,
                previous_agent = 56,
                previous_agent_status = 'success',
                previous_agent_output = ''
            )
        else:
            return PatchedPeriodicAgentCreate(
        )
        """

    def testPatchedPeriodicAgentCreate(self):
        """Test PatchedPeriodicAgentCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
