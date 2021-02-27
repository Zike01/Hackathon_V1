"""
12 - Create a function that will take a string of text and return the index number of each letter in
the alphabet. For instance, if the input is “abc” it should return “1 2 3”; if the input is “xyz” it
should return “24 25 26”.
"""


def find_index(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    indexes = ""
    for t in text:
        # Loop through the alphabet for each character in the string input.
        for char in alphabet:
            if t.lower() == char:
                # Finds the index+1 of the given char in the alphabet and converts it into a string.
                indexes += str(alphabet.index(t.lower()) + 1)
                indexes += " "

    return indexes


string = input("Enter a string of text: ")
print(find_index(string))
