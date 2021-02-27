"""
14 - Write a program that can take a list of numbers. If a number in the list is an even number it
should be added to a running total, if the number is odd it should be ignored. After processing all
the numbers in the list it should output the total (i.e. the sum of all the even numbers in the list).

"""


def sum_of_even(number_list):
    total = 0
    for n in number_list:
        if n % 2 == 0:
            total += n

    return total


# EXAMPLE
print(f"The sum of the even numbers is {sum_of_even([23, 345, 41, 456, 46, 41, 67, 68, 90])}")
