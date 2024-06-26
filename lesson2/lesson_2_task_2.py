def is_year_leap(year):
    return year % 4 == 0
year_str = input("Введите год: ")
year_int = int(year_str)
print("год", year_str + ":", is_year_leap(year_int))
