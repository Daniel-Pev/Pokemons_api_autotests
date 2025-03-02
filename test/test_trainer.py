"""
Tests for trainer API
"""

import allure

from config.base_test import BaseTest


@allure.epic("Battle")
@allure.feature("Trainer")
class TestTrainerAPi(BaseTest):

    @allure.step("Get trainer by trainer ID")
    def test_get_trainer_by_id(self):
        """
        Test for getting trainer by trainer ID
        """
        self.api_trainer.get_trainer_by_trainer_id()

    @allure.step("Change trainer")
    def test_change_trainer(self):
        """
        Test for changing trainer
        """
        self.api_trainer.change_trainer()
