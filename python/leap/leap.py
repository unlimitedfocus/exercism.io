def is_leap_year(year):
    div_4 = (year % 4 == 0)
    div_100 = (year % 100 == 0)
    div_400 = (year % 400 == 0)

    return div_4 and ((div_100 and div_400) or (not div_100 and not div_400))
