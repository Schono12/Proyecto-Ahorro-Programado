# ===== interfaz_consola.py =====

import srs.model.logica_ahorro as logica_ahorro


def pedir_float(mensaje):
    """Solicita un número decimal al usuario."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("ERROR: Debe ingresar un número válido.")


def pedir_int(mensaje):
    """Solicita un número entero al usuario."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("ERROR: Debe ingresar un número entero válido.")


def preguntar_abono():
    """Pregunta si desea agregar abono extra."""
    opcion = input("¿Desea agregar un abono extra? (si/no): ").strip().lower()

    if opcion == "si":
        abono = pedir_float("Ingrese el valor del abono extra: ")
        mes = pedir_int("Ingrese el mes en que realizará el abono: ")
        return abono, mes

    return 0, None


def mostrar_menu():
    print("\n====== AHORRO PROGRAMADO ======")
    print("1. Calcular cuota mensual")
    print("2. Calcular total intereses")
    print("3. Salir")


def interfaz():
    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "3":
            print("Saliendo del programa...")
            break

        if opcion not in ["1", "2"]:
            print("Opción inválida.")
            continue

        print("\nIngrese los datos del ahorro")

        meta = pedir_float("Meta de ahorro: ")
        interes = float(pedir_float("Tasa de interés (ej: 1 para 1%, 0.75 para 0.75%): ") / 100)
        plazo = pedir_int("Plazo en meses: ")

        abono, mes_abono = preguntar_abono()

        try:

            if opcion == "1":
                cuota = logica_ahorro.calcular_cuota(
                    meta,
                    interes,
                    plazo,
                    abono,
                    mes_abono
                )

                print("\n===== RESULTADO =====")
                print(f"Cuota mensual necesaria: ${cuota:,.2f}")

            elif opcion == "2":

                total_interes = logica_ahorro.calcular_total_interes(
                    meta,
                    interes,
                    plazo,
                    abono,
                    mes_abono
                )

                print("\n===== RESULTADO =====")
                print(f"Total intereses generados: ${total_interes:,.2f}")

        except Exception as e:
            print("\nSe produjo un error:")
            print(e)


if __name__ == "__main__":
    interfaz()