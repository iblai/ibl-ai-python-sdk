# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.paginated_ai_generated_image_list import PaginatedAIGeneratedImageList

class TestPaginatedAIGeneratedImageList(unittest.TestCase):
    """PaginatedAIGeneratedImageList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedAIGeneratedImageList:
        """Test PaginatedAIGeneratedImageList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedAIGeneratedImageList`
        """
        model = PaginatedAIGeneratedImageList()
        if include_optional:
            return PaginatedAIGeneratedImageList(
                count = 123,
                next = 'http://api.example.org/accounts/?page=4',
                previous = 'http://api.example.org/accounts/?page=2',
                results = [
                    iblai.models.ai_generated_image.AIGeneratedImage(
                        id = 56, 
                        user = 56, 
                        image = '', 
                        platform = 56, 
                        prompt = '', 
                        model = '', 
                        provider = '', 
                        date_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return PaginatedAIGeneratedImageList(
        )
        """

    def testPaginatedAIGeneratedImageList(self):
        """Test PaginatedAIGeneratedImageList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()