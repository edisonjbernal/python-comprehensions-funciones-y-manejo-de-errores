dict = {}

for i in range(1,5):
    dict[i] = i * 2

print(dict)
#{1: 2, 2: 2, 3: 2, 4: 2}

dict_with_comprehention = {i:i * 2 for i in range(1,5)}
print(dict_with_comprehention)
#{1: 2, 2: 2, 3: 2, 4: 2}

import random

countries = ['col','mex','bol','pe']
population = {}
for country in countries:
    population[country] = random.randint(1000,8000)
print(population)

population_with_comprehention = {country:random.randint(1000,8000) for country in countries }
print(population_with_comprehention)

names = ['Camilo','Juan','Pedro']
ages = [33,24,13]
#Une dos listas en una con tuplas
print(list(zip(names,ages)))
#[('Camilo', 33), ('Juan', 24), ('Pedro', 13)]

# Esta me generó un diccionario
new_dict = {name:age for (name,age) in zip(names,ages)}
print(new_dict)
#{'Camilo': 33, 'Juan': 24, 'Pedro': 13}