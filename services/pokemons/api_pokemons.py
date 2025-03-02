"""
This module contains methods for working with the Pokemons API
"""

import os

import allure
import requests
from dotenv import load_dotenv

from config.headers import Headers
from services.pokemons.endpoints import EndpointsPokemons
from services.pokemons.models.pokemons_model import PokemonsCreateModel, PokemonsGetModel, PokemonsDeleteModel, \
    PokemonsChangeModel
from services.pokemons.payloads import Payloads
from utils.helper import Helper

load_dotenv()

TRAINER_ID = os.getenv('TRAINER_ID_PROD') if os.environ["STAGE"] == "PROD" else os.getenv('TRAINER_ID_DEV')


class PokemonsAPI(Helper):
    """
    Class for working with the Pokemons API
    """

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = EndpointsPokemons()
        self.headers = Headers()

    @allure.step("Create pokemon")
    def create_pokemon(self):
        """
        Create pokemon
        """
        response = requests.post(
            url=self.endpoints.create_pokemon,
            headers=self.headers.basic,
            json=self.payloads.create_pokemon
        )
        assert response.status_code == 201, response.json()
        self.attach_response(response.json())
        self.log(response, self.payloads.create_pokemon)
        model = PokemonsCreateModel(**response.json())
        return model

    @allure.step("Change pokemon")
    def change_pokemon(self, pokemon_id):
        """
        Change pokemon

        """
        response = requests.put(
            url=self.endpoints.change_pokemon,
            headers=self.headers.basic,
            json=self.payloads.change_pokemon(pokemon_id)
        )
        assert response.status_code == 200, response.json()

        assert response.json()['id'] == self.payloads.change_pokemon(pokemon_id)['pokemon_id'], response.json()
        self.attach_response(response.json())
        self.log(response, self.payloads.change_pokemon(pokemon_id))
        model = PokemonsChangeModel(**response.json())
        return model

    @allure.step("delete pokemon")
    def delete_pokemon(self, pokemon_id):
        """
        Delete pokemon

        """
        response = requests.post(
            url=self.endpoints.delete_pokemon,
            headers=self.headers.basic,
            json=self.payloads.delete_pokemon(pokemon_id)
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        self.log(response, self.payloads.delete_pokemon(pokemon_id))
        model = PokemonsDeleteModel(**response.json())
        return model

    @allure.step("Get pokemon by trainer ID")
    def get_pokemon_by_trainer_id(self, trainer_id=None):
        """
        Get pokemon by trainer ID

        """
        if trainer_id is None:
            trainer_id = TRAINER_ID
        response = requests.get(
            url=self.endpoints.get_pokemons_by_trainer_id(trainer_id),
            headers=self.headers.basic,
        )
        assert response.status_code == 200, response.json()
        assert response.json()['data'][0]['trainer_id'] == trainer_id, response.json()
        self.attach_response(response.json())
        self.log(response)
        model = PokemonsGetModel(**response.json())
        return model
