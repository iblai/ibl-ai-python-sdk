# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.user_chat_feedback import UserChatFeedback

class TestUserChatFeedback(unittest.TestCase):
    """UserChatFeedback unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserChatFeedback:
        """Test UserChatFeedback
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserChatFeedback`
        """
        model = UserChatFeedback()
        if include_optional:
            return UserChatFeedback(
                id = 56,
                username = '',
                session = '',
                user_text = '',
                ai_response = '',
                reason = '',
                additional_feedback = '',
                rating = 1,
                inserted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                mentor = 56
            )
        else:
            return UserChatFeedback(
                id = 56,
                username = '',
                session = '',
                user_text = '',
                ai_response = '',
                reason = '',
                additional_feedback = '',
                mentor = 56,
        )
        """

    def testUserChatFeedback(self):
        """Test UserChatFeedback"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
