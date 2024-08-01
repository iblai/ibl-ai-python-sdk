# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.videos_watched_sub_section import VideosWatchedSubSection

class TestVideosWatchedSubSection(unittest.TestCase):
    """VideosWatchedSubSection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VideosWatchedSubSection:
        """Test VideosWatchedSubSection
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VideosWatchedSubSection`
        """
        model = VideosWatchedSubSection()
        if include_optional:
            return VideosWatchedSubSection(
                display_name = '',
                id = '',
                total_watch = '',
                videos = [
                    iblai.models.video_block.VideoBlock(
                        display_name = '', 
                        id = '', 
                        total_users = 56, )
                    ]
            )
        else:
            return VideosWatchedSubSection(
                display_name = '',
                id = '',
                total_watch = '',
        )
        """

    def testVideosWatchedSubSection(self):
        """Test VideosWatchedSubSection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
