"""
Payloads for pokemons API

"""

from faker import Faker

fake = Faker('ru_RU')


class Payloads:
    """
    Class that contains payloads for pokemons API.
    """

    create_pokemon = {
        "name": fake.first_name(),
        "photo_id": fake.random_int(min=1, max=1008),
    }


    @staticmethod
    def delete_pokemon(pokemon_id):
        """
        Returns payload for deleting a pokemon.

        """
        return {
            "pokemon_id": pokemon_id
        }

    @staticmethod
    def change_pokemon(pokemon_id):
        """
        Returns payload for changing a pokemon.

        """
        return {
            "pokemon_id": pokemon_id,
            "name": fake.first_name(),
            "photo_id": fake.random_int(min=1, max=1008),
        }