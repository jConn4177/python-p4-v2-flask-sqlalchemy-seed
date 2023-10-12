#!/usr/bin/env python3
# server/seed.py
from random import choice as rc
from faker import Faker

from app import app
from models import db, Pet

with app.app_context():

    # Create and initialize a faker generator
    fake = Faker()

    # Delete all rows in the "pets" table
    Pet.query.delete()

    # Create an empty list
    pets = []

    species = ['Dog', 'Cat', 'Chicken', 'Rat', 'Porcupine']

    # Add some Pet instances to the list
    for n in range(10):
        pet = Pet(name=fake.first_name(), species=rc(species))
        pets.append(pet)

    # # Add some Pet instances to the list
    # pets.append(Pet(name="Lucy", species="Dog"))
    # pets.append(Pet(name="Sam", species="Cat"))
    # pets.append(Pet(name="Penny", species="Porcupine"))
    # pets.append(Pet(name="Kip", species="Rat"))

    # Insert each Pet in the list into the database table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()
