def get_city_population(populations, city):
    try:
        population = populations[city]
        print(f"The population of {city}, which is {population} in this dictionary.")

    except KeyError:
        raise KeyError(f'City "{city}" not found in population data.')


city_populations = {"New York": 8336817, "Los Angeles": 3979576, "Chicago": 2679044}

# city_name = "New York"
city_name = "Tampa"
get_city_population(city_populations, city_name)
