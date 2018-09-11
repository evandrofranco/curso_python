def is_leap_year(year):
    leap_year = False
    if ((year % 4 == 0) and (not (year % 100 == 0))) or (year % 400 == 0):
        leap_year = True
    return leap_year


print('2010:', is_leap_year(2010))

print('2016:', is_leap_year(2016))

print('2000:', is_leap_year(2000))
