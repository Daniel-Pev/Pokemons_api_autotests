"""
Tests for API endpoints related to pokemons
"""

import allure

from config.base_test import BaseTest


@allure.epic("Battle")
@allure.feature("Pokemons")
class TestPokemonsAPI(BaseTest):

    @allure.step("Create pokemon")
    def test_create_pokemon(self, setup_pokemons):
        """
        Test that pokemon can be created
        """
        self.api_pokemons.create_pokemon()

    @allure.step("Delete pokemon")
    def test_delete_pokemon(self, setup_pokemons):
        """
        Test that pokemon can be deleted
        """
        pokemon = self.api_pokemons.create_pokemon()
        self.api_pokemons.delete_pokemon(pokemon_id=str(pokemon.id))

    @allure.step("Change pokemon")
    def test_change_pokemon(self, setup_pokemons):
        """
        Test that pokemon can be changed
        """
        pokemon = self.api_pokemons.create_pokemon()
        self.api_pokemons.change_pokemon(pokemon_id=str(pokemon.id))

    @allure.step("Get pokemon by trainer ID")
    def test_get_pokemon_by_trainer_id(self, setup_pokemons):
        """
        Test that pokemons can be retrieved by trainer id
        """
        self.api_pokemons.get_pokemon_by_trainer_id()
