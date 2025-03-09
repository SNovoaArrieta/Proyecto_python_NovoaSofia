from Modules.data_management import load_data
from Modules.report_generation import get_population_data_by_country, get_population_growth
from Modules.utils import format_report

def mostrar_menu():
    print("\n--- Menú de Opciones ---")
    print("1. Obtener datos de población para un país en un rango de años.")
    print("2. Calcular el crecimiento poblacional de un país.")
    print("3. Salir.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1, 2 o 3): ")

        if opcion == "1":
            # Opción 1: Obtener datos de población
            country_code = input("Ingresa el código ISO3 del país (por ejemplo, IND para India): ").upper()
            start_year = int(input("Ingresa el año de inicio (por ejemplo, 2000): "))
            end_year = int(input("Ingresa el año de fin (por ejemplo, 2023): "))

            try:
                population_data = get_population_data_by_country(country_code, start_year, end_year)
                if population_data:
                    print(f"\nDatos de población para {country_code} ({start_year}-{end_year}):")
                    format_report(population_data)
                else:
                    print(f"No se encontraron datos para {country_code} en el rango de años especificado.")
            except Exception as e:
                print(f"Ocurrió un error: {e}")

        elif opcion == "2":
            # Opción 2: Calcular crecimiento poblacional
            country_code = input("Ingresa el código ISO3 del país (por ejemplo, IND para India): ").upper()

            try:
                growth_data = get_population_growth(country_code)
                if growth_data:
                    print(f"\nCrecimiento poblacional para {country_code}:")
                    for entry in growth_data:
                        print(f"Año: {entry['ano']}, Crecimiento: {entry['crecimiento']:.2f}%")
                else:
                    print(f"No se encontraron datos de crecimiento para {country_code}.")
            except Exception as e:
                print(f"Ocurrió un error: {e}")

        elif opcion == "3":
            # Opción 3: Salir
            print("¡Gracias por usar el sistema! ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

if __name__ == "__main__":
    main()