import re

def get_population():
    keys = ['col','bol']
    values = [300,400]
    return keys,values

def get_population_by_country(country):
    population_dic = {}
    for key, value in country.items():
        if "Population" in key:
            if key != "World Population Percentage":
                number = re.findall(r"\d+", key)
                new_key = number[0]
                population_dic[new_key] = int(value)

    labels = population_dic.keys()
    values = population_dic.values()
    return labels,values



def population_by_country(data,country):
    return list(filter(lambda item:item['Country/Territory'] == country,data))

