"""
7 - Write a function that will take as an input a person’s forename, surname, age, marital status
and gender, and the output an appropriate salutation. For instance, if the input is [“Osamu”,
“Dazai”, 21, “single”, “male”], it should output “Dear Mr Osamu Dazai”. If the input is [“Lucy
Maud”, “Montgomery”, 50, “married”, “female”], it should output “Dear Mrs Lucy Maud
Montgomery”. The full list of possible titles are [“Miss”, “Master”, “Mrs”, “Miss”, “Mr”].
"""


def salutation(attributes):
    person = {
        "forename": attributes[0],
        "surname": attributes[1],
        "age": attributes[2],
        "marital status": attributes[3],
        "gender": attributes[4]
    }
    if person["gender"].lower() == "female":
        if person["marital status"].lower() == "married":
            pronoun = "Mrs"
        else:
            pronoun = "Miss"
    else:
        pronoun = "Mr"

    return f'Dear {pronoun} {person["forename"].title()} {person["surname"].title()}'


personal_info = ['Osamu', 'Dazai', 21, 'single', 'male']
print(salutation(personal_info))

lady_info = ['Lucy Maud', 'Montgomery', 50, 'married', 'female']
print(salutation(lady_info))

