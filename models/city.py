#!/usr/bin/python3


"""
This module will define City class that will inherate from base model
its attributes/methods
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class
    """

    state_id = ""
    name = ""
