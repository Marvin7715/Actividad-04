from datetime import date

name = input("Ingrese su nombre completo: ")
dpi = input("Ingrese su número de DPI (13 dígitos): ")
departament = input("Ingrese su departamento: ")
year_of_birth = input("Ingrese su año de nacimiento (YYYY): ")

if len(name.replace(" ", "")) < 5:
    print("Nombre inválido. Debe tener al menos 5 letras.")
    exit()

if not dpi.isdigit() or len(dpi) != 13:
    print("DPI inválido. Debe contener exactamente 13 dígitos numéricos.")
    exit()

if not year_of_birth.isdigit() or len(year_of_birth) != 4:
    print("Año de nacimiento inválido. Debe tener 4 dígitos.")
    exit()

year_of_birth = int(year_of_birth)
current_year = date.today().year

if year_of_birth < 1900 or year_of_birth > current_year:
    print("Año de nacimiento fuera de rango.")
    exit()

age = current_year - year_of_birth
can_vote = False

if age >= 18:
    can_vote = True
elif departament in ["petén", "alta verapaz"] and age >= 17:
    can_vote = True

if can_vote:
    print(f"Bienvenido {name}, su centro de votación está en {departament.capitalize()}")
else:
    print("Lo sentimos, aún no puede votar.")