# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.api.search_api import SearchApi


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SearchApi()

    def tearDown(self) -> None:
        pass

    def test_search_ai_search_detail_retrieve(self) -> None:
        """Test case for search_ai_search_detail_retrieve

        """
        pass

    def test_search_ai_search_retrieve(self) -> None:
        """Test case for search_ai_search_retrieve

        """
        pass

    def test_search_documentsearch_retrieve(self) -> None:
        """Test case for search_documentsearch_retrieve

        """
        pass

    def test_search_es_health_retrieve(self) -> None:
        """Test case for search_es_health_retrieve

        """
        pass

    def test_search_search_retrieve(self) -> None:
        """Test case for search_search_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
