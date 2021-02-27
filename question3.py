"""
3 - Write a function that can take as an input a date/time in UTC (https://en.wikipedia.org/wiki/
Coordinated_Universal_Time) and a desired timezone to change the time to (this should include
the main four US timezones, (https://en.wikipedia.org/wiki/
Time_in_the_United_States#United_States_time_zones) Pacific, Mountain, Central and Eastern;
China time; and British Summer Time. An example input may be “18/02/2020 23:30” and “ET”.
"""

from datetime import datetime, timedelta


def change_timezone(date, time_zone):
    """
    Change to desired timezone
    """
    if time_zone.upper() == "ET":
        date -= timedelta(hours=5)
    elif time_zone.upper() == "CT":
        date -= timedelta(hours=6)
    elif time_zone.upper() == "MT":
        date -= timedelta(hours=7)
    elif time_zone.upper() == "PT":
        date -= timedelta(hours=8)
    else:
        return "Not a valid timezone, please try again."

    return date.strftime("%d/%m/%Y %H:%M")


date_string = input("Enter the date (DD/MM/YYYY): ")
time_string = input("Enter the UTC time in the 24hr format (HH:MM): ")

# Convert the date and time string input to a datetime object.
date_UTC = datetime.strptime(date_string + " " + time_string, "%d/%m/%Y %H:%M")

# Allow the user to choose a timezone.
timezone = input("Pacific: PT\n"
                 "Mountain: MT\n"
                 "Central: CT\n"
                 "Eastern: ET\n"
                 "Choose the timezone: ")

output = change_timezone(date_UTC, timezone)
change_timezone()
print(output)
