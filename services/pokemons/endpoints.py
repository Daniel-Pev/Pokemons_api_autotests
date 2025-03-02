"""
Endpoints for Pokemons API
"""

import os

HOST = "https://api.pokemonbattle.ru/v2" if os.environ["STAGE"] == "PROD" else "https://api.pokemonbattle-stage.ru/v2"


class EndpointsPokemons:
    """
    Endpoints for Pokemons API
    """

    create_pokemon = f"{HOST}/pokemons"

    get_pokemons = f"{HOST}/pokemons"

    change_pokemon = f"{HOST}/pokemons"

    partly_change_pokemon = f"{HOST}/pokemons"

    delete_pokemon = f"{HOST}/pokemons/knockout"

    @staticmethod
    def get_pokemons_by_id(pokemon_id):
        """
        Get pokemon by id
        """
        return f"{HOST}/pokemons?pokemon_id={pokemon_id}"

    @staticmethod
    def get_pokemons_by_name(pokemon_name):
        """
        Get pokemon by name


        """
        return f"{HOST}/pokemons?name={pokemon_name}"

    @staticmethod
    def get_pokemons_by_trainer_id(trainer_id):
        """
        Get pokemons by trainer id
        """
        return f"{HOST}/pokemons?trainer_id={trainer_id}"
