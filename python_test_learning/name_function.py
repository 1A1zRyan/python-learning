def get_formatted_name(city, country, population=''):
    """Get formatted name"""

    if population:
        full_name = city + ',' + country + '-population: ' + str(population)
    else:
        full_name = city + ',' + country
    return full_name.title()