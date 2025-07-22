from datetime import date

day = int(input("Ingresa el día: "))
month = int(input("Ingresa el mes (en números): "))
year = int(input("Ingresa el año: "))

valid = True

if month in [1, 3, 5, 7, 8, 10, 12]:
    if day < 1 or day > 31:
        valid = False
elif month in [4, 6, 9, 11]:
    if day < 1 or day > 30:
        valid = False
elif month == 2:
    leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if leap:
        if day < 1 or day > 29:
            valid = False
    else:
        if day < 1 or day > 28:
            valid = False
else:
    valid = False

if not valid:
    print("¡Fecha inválida!")
else:
    m = month
    y = year
    if m < 3:
        m += 12
        y -= 1

    k = y % 100
    j = y // 100

    h = (day + (13 * (m + 1)) // 5 + k + (k // 4) + (j // 4) + 5 * j) % 7

    weekdays = ["sábado", "domingo", "lunes", "martes", "miércoles", "jueves", "viernes"]
    weekday = weekdays[h]

    input_date = date(year, month, day)
    today = date.today()

    if input_date == today:
        print(f"La fecha {day:02d}/{month:02d}/{year} es hoy, {weekday}.")
    elif input_date < today:
        print(f"La fecha {day:02d}/{month:02d}/{year} fue un {weekday}.")
        print(f"La fecha {day:02d}/{month:02d}/{year} ya pasó.")
    else:
        print(f"La fecha {day:02d}/{month:02d}/{year} será un {weekday}.")
        print(f"La fecha {day:02d}/{month:02d}/{year} aún no ha llegado.")