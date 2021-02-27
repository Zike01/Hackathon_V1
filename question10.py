"""
10 - Create a function that takes time in the 24-hour clock (e.g. “23:30”) and converts to the 12-
hour clock (e.g. “11:30 PM”). Print the result to screen.
"""


def convert_time(twenty_four_hour_time):
    hour = int(twenty_four_hour_time.split(":")[0])
    minute = int(twenty_four_hour_time.split(":")[1])

    if hour < 0 or hour > 23 or minute < 0 or minute > 59:
        return "Invalid time"
    elif hour < 12:
        abbreviation = "AM"
        if hour == 0:
            hour += 12
    else:
        abbreviation = "PM"
        if hour > 12:
            hour -= 12

    return f"24-hour time: {twenty_four_hour_time}\n" \
           f"12-hour time: {hour}:{minute:02d} {abbreviation}"


time = input("Enter time in the 24-hour format: ")
print(convert_time(time))


