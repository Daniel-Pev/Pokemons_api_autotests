"""
This module contains headers for API requests.

"""

import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN_PROD') if os.environ["STAGE"] == "PROD" else os.getenv('TOKEN_DEV')


class Headers:
    """
    This class contains the headers for API requests.
    """

    basic = {
        'Content-Type': 'application/json',
        "trainer_token": TOKEN
    }
