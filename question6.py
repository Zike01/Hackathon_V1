"""
6 - Write a function that will round a float in reverse. If the input has a decimal greater than or
equal to .5 then in should round down. If the decimal is less than .5 it should round up.
"""

import math


def reverse_round(num):
    # int(num) rounds the number down to the nearest integer
    if num - int(num) >= 0.5:
        rounded_num = math.floor(num)
    else:
        rounded_num = math.ceil(num)

    return rounded_num


print(reverse_round(5.667))
print(reverse_round(6.21))
