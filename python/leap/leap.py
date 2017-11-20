def is_leap_year(year):
    div_4 = (year % 4 == 0)
    div_100 = (year % 100 == 0)
    div_400 = (year % 400 == 0)

    if div_4:
        if div_100 and div_400:
            return True
        elif div_100 and not div_400:
            return False
        elif not div_400 and not div_100:
            return True
        else:
            return False
    else:
        return False
