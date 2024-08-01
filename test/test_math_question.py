# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.math_question import MathQuestion

class TestMathQuestion(unittest.TestCase):
    """MathQuestion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MathQuestion:
        """Test MathQuestion
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MathQuestion`
        """
        model = MathQuestion()
        if include_optional:
            return MathQuestion(
                id = 56,
                topic = iblai.models.topic.Topic(
                    total_topics = 56, 
                    number_of_messages = 56, 
                    topic_detail = [
                        iblai.models.topic_detail.TopicDetail(
                            id = 56, 
                            total_topics = 56, 
                            number_of_messages = 56, 
                            number_of_conversations = 56, 
                            user_sentiment = '', 
                            user_ratings = '', 
                            name = '', 
                            metadata = null, 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            platform = 56, )
                        ], 
                    monthly_total_topics_diff = 56, ),
                sub_topic = iblai.models.sub_topic.SubTopic(
                    id = 56, 
                    topic = iblai.models.topic.Topic(
                        total_topics = 56, 
                        number_of_messages = 56, 
                        topic_detail = [
                            iblai.models.topic_detail.TopicDetail(
                                id = 56, 
                                total_topics = 56, 
                                number_of_messages = 56, 
                                number_of_conversations = 56, 
                                user_sentiment = '', 
                                user_ratings = '', 
                                name = '', 
                                metadata = null, 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                platform = 56, )
                            ], 
                        monthly_total_topics_diff = 56, ), 
                    name = '', ),
                skills_assessed = [
                    iblai.models.skill.Skill(
                        id = 56, 
                        name = '', )
                    ],
                content = '',
                difficulty = 0,
                cognitive_skills = None,
                grade = 1,
                expected_time_to_solve = '',
                related_concepts = '',
                hints_provided = '',
                learning_outcomes = '',
                prerequisites = '',
                recommended_grade_level = '',
                image = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                platform = 56
            )
        else:
            return MathQuestion(
                id = 56,
                topic = iblai.models.topic.Topic(
                    total_topics = 56, 
                    number_of_messages = 56, 
                    topic_detail = [
                        iblai.models.topic_detail.TopicDetail(
                            id = 56, 
                            total_topics = 56, 
                            number_of_messages = 56, 
                            number_of_conversations = 56, 
                            user_sentiment = '', 
                            user_ratings = '', 
                            name = '', 
                            metadata = null, 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            platform = 56, )
                        ], 
                    monthly_total_topics_diff = 56, ),
                sub_topic = iblai.models.sub_topic.SubTopic(
                    id = 56, 
                    topic = iblai.models.topic.Topic(
                        total_topics = 56, 
                        number_of_messages = 56, 
                        topic_detail = [
                            iblai.models.topic_detail.TopicDetail(
                                id = 56, 
                                total_topics = 56, 
                                number_of_messages = 56, 
                                number_of_conversations = 56, 
                                user_sentiment = '', 
                                user_ratings = '', 
                                name = '', 
                                metadata = null, 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                platform = 56, )
                            ], 
                        monthly_total_topics_diff = 56, ), 
                    name = '', ),
                skills_assessed = [
                    iblai.models.skill.Skill(
                        id = 56, 
                        name = '', )
                    ],
                content = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testMathQuestion(self):
        """Test MathQuestion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
