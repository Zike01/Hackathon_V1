"""
15 - Write a function that can take two numbers as an input. The function should divide the first
number by the second number and establish if the output is an integer (whole number) or decimal.
For instance, if the input is “4” and “2”, the output should be “integer” (the answer is 2). If the
input is “3” and “2” the output should be “decimal” (the answer is 1.5).

"""


def int_or_float(num1, num2):
    output = num1/num2

    # int(output) rounds the number down to the nearest integer.
    if output - int(output) == 0:
        return "an integer"
    else:
        return "a decimal"


first_number = int(input("First Number: "))
second_number = int(input("Second Number: "))
answer = int_or_float(first_number, second_number)

print(f"The answer is {answer}")


