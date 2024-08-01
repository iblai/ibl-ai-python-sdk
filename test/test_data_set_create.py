# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.data_set_create import DataSetCreate

class TestDataSetCreate(unittest.TestCase):
    """DataSetCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataSetCreate:
        """Test DataSetCreate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataSetCreate`
        """
        model = DataSetCreate()
        if include_optional:
            return DataSetCreate(
                id = '',
                name = '',
                source_url = '',
                source_file = '',
                num_data_points = 0,
                train_split = 0,
                prompt = ''
            )
        else:
            return DataSetCreate(
                id = '',
                name = '',
        )
        """

    def testDataSetCreate(self):
        """Test DataSetCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()