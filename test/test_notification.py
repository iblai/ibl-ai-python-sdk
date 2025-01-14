# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.notification import Notification

class TestNotification(unittest.TestCase):
    """Notification unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Notification:
        """Test Notification
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Notification`
        """
        model = Notification()
        if include_optional:
            return Notification(
                id = '',
                username = '',
                title = '',
                body = '',
                status = None,
                channel = 56,
                context = None,
                short_message = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return Notification(
                id = '',
                username = '',
                title = '',
                body = '',
                short_message = '',
        )
        """

    def testNotification(self):
        """Test Notification"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
