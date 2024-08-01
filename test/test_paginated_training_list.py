# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.paginated_training_list import PaginatedTrainingList

class TestPaginatedTrainingList(unittest.TestCase):
    """PaginatedTrainingList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedTrainingList:
        """Test PaginatedTrainingList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedTrainingList`
        """
        model = PaginatedTrainingList()
        if include_optional:
            return PaginatedTrainingList(
                count = 123,
                next = 'http://api.example.org/accounts/?page=4',
                previous = 'http://api.example.org/accounts/?page=2',
                results = [
                    iblai.models.training.Training(
                        id = '', 
                        dataset = iblai.models.data_set.DataSet(
                            id = '', 
                            platform = {
                                'key' : null
                                }, 
                            name = '', 
                            prompt = '', 
                            source_url = '', 
                            source_file = '', 
                            status = 'pending', 
                            num_data_points = 0, 
                            train_split = 0, 
                            train_file = '', 
                            test_file = '', 
                            retry_attempts = 0, 
                            error_log = '', 
                            date_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            last_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        project_name = '', 
                        metadata = null, 
                        status = 'pending', 
                        retry_attempts = 0, 
                        fine_tuned_model = '', 
                        provider = 'openai', 
                        base_model_name = '', 
                        text_column = '', 
                        learning_rate = 1.337, 
                        batch_size = 0, 
                        num_epochs = 0, 
                        block_size = 0, 
                        warmup_ratio = 1.337, 
                        lora_r = 0, 
                        lora_alpha = 0, 
                        lora_dropout = 1.337, 
                        weight_decay = 1.337, 
                        gradient_accumulation = 0, 
                        use_peft = True, 
                        use_fp16 = True, 
                        use_int4 = True, 
                        push_to_hub = True, 
                        repo_id = '', 
                        preprocess_dataset = True, 
                        prompt_column = '', 
                        response_column = '', 
                        prompt_prefix = '', 
                        prompt_suffix = '', 
                        response_prefix = '', 
                        response_suffix = '', 
                        error_log = '', 
                        date_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        platform = 56, )
                    ]
            )
        else:
            return PaginatedTrainingList(
        )
        """

    def testPaginatedTrainingList(self):
        """Test PaginatedTrainingList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
