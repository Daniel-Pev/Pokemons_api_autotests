"""
Models for pokemons API
"""


from pydantic import BaseModel, model_validator, field_validator, Field


class PokemonsCreateModel(BaseModel):
    """
    Model for creating pokemon
    """

    message: str
    id: int

    @model_validator(mode='before')
    def fields_are_not_empty(self, value):
        """
        Check that fields are not empty
        """
        if value == "" or value is None:
            raise Exception("Field is empty")
        else:
            return self

    @field_validator('message')
    def check_message(cls, value):
        """
        Check that message is correct
        """
        if value != 'Покемон создан':
            raise Exception("Message is not correct")
        return value


class PokemonsGetModel(BaseModel):
    """
    Model for getting pokemon
    """

    status: str
    data: list
    next_page: bool

    @model_validator(mode='before')
    def fields_are_not_empty(self, value):
        """
        Check that fields are not empty
        """
        if value == "" or value is None:
            raise Exception("Field is empty")
        else:
            return self

    @field_validator('status')
    def check_message(cls, value):
        """
        Check that message is correct
        """
        if value != 'success':
            raise Exception("Message is not correct")
        return value


class PokemonsChangeModel(BaseModel):
    """
    Model for changing pokemon
    """

    message: str
    id: int

    @model_validator(mode='before')
    def fields_are_not_empty(self, value):
        """
        Check that fields are not empty
        """
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return self

    @field_validator('message')
    def check_message(cls, value):
        """
        Check that message is correct
        """
        if value != 'Информация о покемоне обновлена':
            raise Exception("Message is not correct")
        return value


class PokemonsDeleteModel(BaseModel):
    """
    Model for deleting pokemon
    """

    message: str = Field(default='Покемон в нокауте')
    id: int

    @model_validator(mode='before')
    def fields_are_not_empty(self, value):
        """
        Check that fields are not empty
        """
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return self

    @field_validator('message')
    def check_message(cls, value):
        """
        Check that message is correct
        """
        if value != 'Покемон в нокауте':
            raise Exception("Message is not correct")
        return value
