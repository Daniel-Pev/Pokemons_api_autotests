"""
Base test class with setup method for api objects
"""

from services.pokemons.api_pokemons import PokemonsAPI
from services.trainers.api_trainer import TrainerAPI


class BaseTest:
    """
    Base test class with setup method for api objects
    """

    def setup_method(self):
        """
        Setup method for api objects
        """
        self.api_pokemons = PokemonsAPI()
        self.api_trainer = TrainerAPI()