# coding=utf-8

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """测试单个答案能被正确存储"""

    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_respnse(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0] , self.my_survey.responses)

    def test_store_three_respnses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()