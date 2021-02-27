"""
16 - Write a program that can take two strings as an input. The program should swap around
every other letter in each string, and return both as an output. For instance, if the input is
“Osamu” and “Dazai”, the output should be “Oaaau” and “Dszmi”. If the two input strings are not
the same length, the outputs should be the length of the shortest string.
"""


def swap_letters(string1, string2):
    str1 = ""
    str2 = ""
    temp = string1

    string1 = [char for char in string1]
    string2 = [char for char in string2]

    if len(string1) <= len(string2):
        shortest_string = string1
    else:
        shortest_string = string2

    for i in range(len(shortest_string)):
        if i % 2 != 0:
            string1[i] = string2[i]
            string2[i] = temp[i]

    return str1.join(string1), str2.join(string2)


print(swap_letters("Osamu", "Dazai"))
