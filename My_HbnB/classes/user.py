#!/usr/bin/python3
from .base_model import BaseModel

class User(BaseModel):
    users = {}  # Class-level dictionary to track users by email

    def __init__(self, email, password, first_name, last_name):
        super().__init__()
        if email in User.users:
            raise ValueError("Email already in use")
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        User.users[email] = self