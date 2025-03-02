"""
Payloads for trainers API

"""


from faker import Faker

fake = Faker()


class Payloads:
    """
    Payloads for trainers API
    """

    @staticmethod
    def change_trainer():
        """
        Payload for changing trainer

        """
        return {
            "name": fake.first_name(),
            "city": fake.city(),
        }
