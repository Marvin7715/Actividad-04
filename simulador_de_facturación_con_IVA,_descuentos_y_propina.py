VAT_RATE = 0.12
DISCOUNT_RATE = 0.10

subtotal = 0.0
tip = 0.0
discount = 0.0

def get_valid_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("El valor no puede ser negativo. Intente de nuevo.")
                continue
            return value
        except ValueError:
            print("Por favor, ingrese un número válido.")

print("Ingrese los precios de los productos. Para terminar, ingrese '0'.")
while True:
    price = get_valid_number("Precio del producto: ")
    if price == 0:
        break
    subtotal += price

tip_response = input("¿Desea dejar propina? (sí/no): ").lower()
if tip_response == 'sí':
    tip_percentage = get_valid_number("¿Cuánto % de propina desea dejar?: ")
    tip = subtotal * (tip_percentage / 100)

card_response = input("¿Tiene tarjeta de cliente frecuente? (sí/no): ").lower()
if card_response == 'sí':
    discount = subtotal * DISCOUNT_RATE

subtotal_with_discount = subtotal - discount
vat = subtotal_with_discount * VAT_RATE
total = subtotal_with_discount + vat + tip

print("\n=== Detalles de la Factura ===")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Descuento (10%): ${discount:.2f}")
print(f"Subtotal con descuento: ${subtotal_with_discount:.2f}")
print(f"IVA (12%): ${vat:.2f}")
print(f"Propina: ${tip:.2f}")
print(f"Total a pagar: ${total:.2f}")