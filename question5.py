"""
5 - Write a function that can take a date input and a person’s date of birth, and then calculate how
old they are. An example input may be “18/02/2020” and “13/06/1981” (returning “38 years old”.
"""
from datetime import datetime
import math


def calculate_age(birth_date):
    date_today = datetime.now()
    num_days = (date_today - birth_date).days
    age = math.floor(num_days/365.25)
    return f"You are {age} years old"


birth_string = input("Enter your date of birth (DD/MM/YYYY): ")

# Convert birthday string to a datetime object.
birthday = datetime.strptime(birth_string, "%d/%m/%Y")

print(calculate_age(birthday))

