MAX_ATTEMPTS = 3

valid_users = {
    "Marvin": "maverick77",
    "Jeshua": "12345678",
    "Byron": "incorrecta"
}

def authenticate_user():
    attempt = 0

    while attempt < MAX_ATTEMPTS:
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")

        if username in valid_users and valid_users[username] == password:
            print("¡Autenticación exitosa!")
            return True

        attempt += 1
        print(f"Intento fallido ({attempt}/{MAX_ATTEMPTS})")

    print("ACCESO BLOQUEADO")
    return False

def show_menu():
    print("MENÚ DE ACCIONES:")
    print("1. Ver perfil")
    print("2. Cambiar contraseña")
    print("3. Cerrar sesión")

def main():
    authenticated = authenticate_user()
    if authenticated:
        show_menu()

main()