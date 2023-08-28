numbers = []

for element in range (1,11):
    numbers.append(element * 2)

print(numbers)
#P [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#Misma sintaxis pero con list comprehentions

numbers_with_list_comprenhentions = [element * 2 for element in range(1,11)]

print(numbers_with_list_comprenhentions)
#P [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#Añadir condicional
numbers = []
for element in range (1,11):
    if element % 2 == 0:
        numbers.append(element * 2)

print(numbers)
#P [4, 8, 12, 16, 20]
#Misma sintaxis pero con list comprehentions
numbers_with_list_comprenhentions = [element * 2 for element in range(1,11) if element % 2 == 0]

print(numbers_with_list_comprenhentions)
#P [4, 8, 12, 16, 20]