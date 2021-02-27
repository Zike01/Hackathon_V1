"""
2 - Write a function that takes in a user string input and reformats it into A E S T H E T I C text.
Example:
Input > Hello World
Output > H e l l o W o r l d
"""


def reformat(input_string):
    output = ""
    for char in input_string:
        output += char
        # Add a space after every char
        output += " "
    return output


string = reformat(input("String: "))
print(string)
