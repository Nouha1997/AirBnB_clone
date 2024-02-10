#!/usr/bin/python3
"""Modules that defines review class."""

from models.base_model import BaseModel

class Review(BaseModel):
    """Class that defines Review instance attribute."""

    place_id = ""
    user_id = ""
    text = ""
