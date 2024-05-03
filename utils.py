


def get_population_by_country(data, country):
    result = list(filter(lambda x: x['Country/Territory'] == country, data))
    return result


def get_population(country_dict):
    population_dict = {
        '2022': float(country_dict['2022 Population'])/1000000,
        '2020': float(country_dict['2020 Population'])/1000000,
        '2015': float(country_dict['2015 Population'])/1000000,
        '2010': float(country_dict['2010 Population'])/1000000,
        '2000': float(country_dict['2000 Population'])/1000000,
        '1990': float(country_dict['1990 Population'])/1000000,
        '1980': float(country_dict['1980 Population'])/1000000,
        '1970': float(country_dict['1970 Population'])/1000000
    } 
    population_dict_asc = {key: population_dict[key] for key in sorted(population_dict)}   
    labels = population_dict_asc.keys()
    values = population_dict_asc.values()
    return labels, values
