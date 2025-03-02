"""
Models for trainers API
"""

from pydantic import BaseModel, model_validator, field_validator


class TrainerGetModel(BaseModel):
    """
    Model for retrieving trainer information.

    """

    status: str
    data: list

    @model_validator(mode='before')
    def fields_are_not_empty(self, value):
        """
        Validates that fields are not empty.

        """
        if value == "" or value is None:
            raise Exception("Field is empty")
        else:
            return self

    @field_validator('status')
    def check_message(cls, value):
        """
        Validates the status message.

        """
        if value != 'success':
            raise Exception("Message is not correct")
        return value


class TrainerChangeModel(BaseModel):
    """
    Model for changing trainer information.

    """

    message: str
    id: str

    @model_validator(mode='before')
    def fields_are_not_empty(self, value):
        """
        Validates that fields are not empty.

        """
        if value == "" or value is None:
            raise Exception("Field is empty")
        else:
            return self

    @field_validator('message')
    def check_message(cls, value):
        """
        Validates the message content.

        """
        if value != 'Информация о тренере обновлена':
            raise Exception("Message is not correct")
        return value
