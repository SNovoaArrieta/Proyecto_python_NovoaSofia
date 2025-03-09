from Modules.data_management import load_data

def get_population_data_by_country(country_code, start_year, end_year):
    # Carga los datos de población
    data = load_data('data/poblacion.json')
    
    # Filtra los datos por país y rango de años
    return [entry for entry in data if entry['codigo_iso3'] == country_code and start_year <= entry['ano'] <= end_year]

def get_population_growth(country_code):
    # Carga los datos de población
    data = load_data('data/poblacion.json')
    
    # Filtra los datos por país
    population_data = [entry for entry in data if entry['codigo_iso3'] == country_code]
    
    # Calcula el crecimiento año a año
    growth_data = []
    for i in range(1, len(population_data)):
        prev_pop = population_data[i-1]['valor']
        curr_pop = population_data[i]['valor']
        growth = ((curr_pop - prev_pop) / prev_pop) * 100
        growth_data.append({
            'ano': population_data[i]['ano'],
            'crecimiento': growth
        })
    return growth_data
