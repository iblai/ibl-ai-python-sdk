# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.train_chat_session_document_view import TrainChatSessionDocumentView

class TestTrainChatSessionDocumentView(unittest.TestCase):
    """TrainChatSessionDocumentView unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrainChatSessionDocumentView:
        """Test TrainChatSessionDocumentView
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrainChatSessionDocumentView`
        """
        model = TrainChatSessionDocumentView()
        if include_optional:
            return TrainChatSessionDocumentView(
                message = ''
            )
        else:
            return TrainChatSessionDocumentView(
                message = '',
        )
        """

    def testTrainChatSessionDocumentView(self):
        """Test TrainChatSessionDocumentView"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
