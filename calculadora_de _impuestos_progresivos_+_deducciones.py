DEPENDENT_DEDUCTION = 1000
TAX_FREE_THRESHOLD = 40000

def calculate_tax(income, dependents):
    if income < TAX_FREE_THRESHOLD and dependents > 2:
        return 0

    taxable_income = income - (dependents * DEPENDENT_DEDUCTION)

    if taxable_income <= 30000:
        tax = taxable_income * 0.05
    elif taxable_income <= 60000:
        tax = 30000 * 0.05 + (taxable_income - 30000) * 0.10
    elif taxable_income <= 100000:
        tax = 30000 * 0.05 + 30000 * 0.10 + (taxable_income - 60000) * 0.15
    else:
        tax = 30000 * 0.05 + 30000 * 0.10 + 40000 * 0.15 + (taxable_income - 100000) * 0.20

    return tax

def main():
    annual_income_input = input("Ingrese su ingreso anual (Q): ")
    number_of_dependents_input = input("Ingrese el número de dependientes: ")

    if not annual_income_input.replace(".", "", 1).isdigit():
        print("Ingreso inválido. Debe ser un número.")
        return

    if not number_of_dependents_input.isdigit():
        print("Número de dependientes inválido. Debe ser un número entero.")
        return

    annual_income = float(annual_income_input)
    number_of_dependents = int(number_of_dependents_input)

    tax_due = calculate_tax(annual_income, number_of_dependents)

    print(f"Su impuesto total a pagar es: Q{tax_due:.2f}")

main()