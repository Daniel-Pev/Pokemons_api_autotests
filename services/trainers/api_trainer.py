"""
This module contains API for trainers.

"""

import allure
import requests
import os
from dotenv import load_dotenv
from config.headers import Headers
from services.trainers.endpoints import EndpointsTrainers
from services.trainers.models.trainer_models import TrainerChangeModel, TrainerGetModel
from services.trainers.payloads import Payloads
from utils.helper import Helper

load_dotenv()

TRAINER_ID = os.getenv('TRAINER_ID_PROD') if os.environ["STAGE"] == "PROD" else os.getenv('TRAINER_ID_DEV')


class TrainerAPI(Helper):
    """
    Class for working with trainers API.
    """

    def __init__(self):
        """
        Initialize TrainerAPI class.
        """
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = EndpointsTrainers()
        self.headers = Headers()

    @allure.step("Change trainer")
    def change_trainer(self):
        """
        Change trainer.

        """
        response = requests.put(
            url=self.endpoints.change_trainer,
            headers=self.headers.basic,
            json=self.payloads.change_trainer()
        )
        assert response.status_code == 200, response.json()

        self.attach_response(response.json())
        self.log(response, self.payloads.change_trainer())
        model = TrainerChangeModel(**response.json())
        return model

    @allure.step("Get trainer by trainer ID")
    def get_trainer_by_trainer_id(self, trainer_id=None):
        """
        Get trainer by its ID.

        """
        if trainer_id is None:
            trainer_id = TRAINER_ID
        response = requests.get(
            url=self.endpoints.get_trainer_by_id(trainer_id),
            headers=self.headers.basic,
        )
        assert response.status_code == 200, response.json()
        assert response.json()['data'][0]['id'] == trainer_id, response.json()
        self.attach_response(response.json())
        self.log(response)
        model = TrainerGetModel(**response.json())
        return model