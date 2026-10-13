# Author : Nhlanhla Radebe

def is_leap_year(year):
    """Checks whether a year is a leap year.
    :param year: the year to check, e.g. 2016
    :return: True if it is a leap year, False if not
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def get_month_code(month):
    """Gives the month code used in step 5 of the algorithm.
    :param month: the month as a number (1-12)
    :return: the month code
    """
    if month == 1:
        return 1
    elif month == 2:
        return 4
    elif month == 3:
        return 4
    elif month == 4:
        return 0
    elif month == 5:
        return 2
    elif month == 6:
        return 5
    elif month == 7:
        return 0
    elif month == 8:
        return 3
    elif month == 9:
        return 6
    elif month == 10:
        return 1
    elif month == 11:
        return 4
    else:
        return 6


def get_century_offset(year):
    """Gives the special offset for the century of the year.
    :param year: the full year, e.g. 1899
    :return: the offset to add (0 if the century has none)
    """
    century = year // 100
    if century == 16:
        return 6
    elif century == 17:
        return 4
    elif century == 18:
        return 2
    elif century == 20:
        return 6
    elif century == 21:
        return 4
    else:
        return 0


def get_day_name(number):
    """Turns the final number (0-6) into a day name.
    :param number: 0 = Saturday, 1 = Sunday ... 6 = Friday
    :return: the name of the day
    """
    if number == 0:
        return "Saturday"
    elif number == 1:
        return "Sunday"
    elif number == 2:
        return "Monday"
    elif number == 3:
        return "Tuesday"
    elif number == 4:
        return "Wednesday"
    elif number == 5:
        return "Thursday"
    else:
        return "Friday"


def get_day_of_the_week(month, day, year):
    """Works out the name of the day of the week for a given date.
    :param month: the month as a number (1-12)
    :param day: the day of the month
    :param year: the full year, e.g. 2022
    :return: the day name, e.g. "Sunday"
    """
    last_two_digits = year % 100
    twelves = last_two_digits // 12
    remainder = last_two_digits % 12
    fours = remainder // 4

    total = twelves + remainder + fours + day + get_month_code(month)

    if is_leap_year(year) and month <= 2:
        total = total + 6

    total = total + get_century_offset(year)

    return get_day_name(total % 7)


def main():
    """Tests get_day_of_the_week against known calendar dates.
    :return: None
    """
    print("Sunday" == get_day_of_the_week(12, 25, 2022))
    print("Friday" == get_day_of_the_week(8, 26, 2022))
    print("Thursday" == get_day_of_the_week(10, 5, 1972))
    print("Wednesday" == get_day_of_the_week(2, 3, 2016))
    print("Monday" == get_day_of_the_week(12, 18, 1899))


# Ensures main() runs ONLY when this file is executed directly
if __name__ == "__main__":
    main()
