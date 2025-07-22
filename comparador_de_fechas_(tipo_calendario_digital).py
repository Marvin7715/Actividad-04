def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 0

def is_valid_date(day, month, year):
    if month < 1 or month > 12:
        return False
    max_day = days_in_month(month, year)
    return 1 <= day <= max_day

def convert_to_days(day, month, year):
    total_days = day
    for y in range(0, year):
        total_days += 366 if is_leap_year(y) else 365
    for m in range(1, month):
        total_days += days_in_month(m, year)
    return total_days

day1 = int(input("Ingresa el día de la primera fecha: "))
month1 = int(input("Ingresa el mes de la primera fecha: "))
year1 = int(input("Ingresa el año de la primera fecha: "))

day2 = int(input("Ingresa el día de la segunda fecha: "))
month2 = int(input("Ingresa el mes de la segunda fecha: "))
year2 = int(input("Ingresa el año de la segunda fecha: "))

if not is_valid_date(day1, month1, year1) or not is_valid_date(day2, month2, year2):
    print("Una o ambas fechas son inválidas.")
else:
    total_days_1 = convert_to_days(day1, month1, year1)
    total_days_2 = convert_to_days(day2, month2, year2)

    if total_days_1 > total_days_2:
        print("La primera fecha es mayor.")
    elif total_days_2 > total_days_1:
        print("La segunda fecha es mayor.")
    else:
        print("Ambas fechas son iguales.")

    if month1 == month2 and year1 == year2:
        print("Ambas fechas están en el mismo mes y año.")
    else:
        print("Las fechas NO están en el mismo mes y año.")

    day_difference = abs(total_days_1 - total_days_2)
    print(f"Es una diferencia significativa de {day_difference} días.")