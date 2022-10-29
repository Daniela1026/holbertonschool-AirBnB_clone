#!/usr/bin/python3
"""
This module will define Review class that will inherate from base model
its attributes/methods
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review Class
    """
    place_id = ""
    user_id = ""
    text = ""
