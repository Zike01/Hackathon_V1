"""
1 - Write a program that will take multiple user inputs, the first being the user's name, followed by
the user's location and finally take something the user likes. Then output a string that contains
this information. e.g.
Output > Hello my name is Jordan, I live in the UK and I like classical music.
"""


name = input("Enter your name: ")
location = input("Enter your location: ")
hobby = input("Hobby: ")

output = f"Hello my name is {name}, I live in {location} and I like {hobby}."
print(output)
