"""
This file contains a fixture for knockout all pokemons before and after test function execution.

"""

import os

import pytest
import requests
from dotenv import load_dotenv

from config.headers import Headers
from services.pokemons.endpoints import EndpointsPokemons
from services.pokemons.payloads import Payloads

load_dotenv()

TRAINER_ID = os.getenv('TRAINER_ID_PROD') if os.environ["STAGE"] == "PROD" else os.getenv('TRAINER_ID_DEV')
def knockout_pokemons():
    """
    Knockout all pokemons
    """

    url = EndpointsPokemons()
    header = Headers().basic
    payload = Payloads()
    pokemons = requests.get(url=url.get_pokemons_by_trainer_id(trainer_id=TRAINER_ID),
                            headers=header)
    if 'data' in pokemons.json():
        for pokemon in pokemons.json()['data']:
            if pokemon['status'] != 0:
                requests.post(url=url.delete_pokemon, headers=header,
                              json=payload.delete_pokemon(pokemon['id']), timeout=3)


@pytest.fixture(scope="function")
def setup_pokemons(request):
    """
    Fixture to knockout all pokemons before and after test function execution.
    """
    knockout_pokemons()
    yield request
    knockout_pokemons()