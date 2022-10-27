#!/usr/bin/python3
"""
This module will define User class that will inherate from base model
its attributes/methods
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Setting new attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
