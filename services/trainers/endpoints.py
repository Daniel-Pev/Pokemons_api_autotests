"""
Endpoints for working with trainers

"""

import os

HOST = "https://api.pokemonbattle.ru/v2" if os.environ["STAGE"] == "PROD" else "https://api.pokemonbattle-stage.ru/v2"


class EndpointsTrainers:
    """
    Endpoints for working with trainers
    """

    get_trainers = f"{HOST}/trainers"
    change_trainer = f"{HOST}/trainers"

    @staticmethod
    def get_trainer_by_id(trainer_id):
        """
        Endpoint for getting a trainer by ID

        """
        return f"{HOST}/trainers?trainer_id={trainer_id}"