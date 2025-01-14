# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.train_document_view_request import TrainDocumentViewRequest

class TestTrainDocumentViewRequest(unittest.TestCase):
    """TrainDocumentViewRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrainDocumentViewRequest:
        """Test TrainDocumentViewRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrainDocumentViewRequest`
        """
        model = TrainDocumentViewRequest()
        if include_optional:
            return TrainDocumentViewRequest(
                pathway = '',
                url = '',
                text = '',
                type = '',
                file = bytes(b'blah'),
                access = 'private',
                branch = '',
                google_drive_auth_data = None,
                dropbox_auth_data = None
            )
        else:
            return TrainDocumentViewRequest(
                pathway = '',
                type = '',
        )
        """

    def testTrainDocumentViewRequest(self):
        """Test TrainDocumentViewRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
