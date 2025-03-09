def format_report(report_data):
    # Muestra los datos de población en un formato legible
    for entry in report_data:
        print(f"Año: {entry['ano']}, Valor: {entry['valor']}")