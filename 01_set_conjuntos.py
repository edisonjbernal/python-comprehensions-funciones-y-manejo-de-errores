set_countries = {'col','mex','bol'}
print(set_countries)
#P {'bol', 'mex', 'col'}
print(type(set_countries))
#P <class 'set'>
set_numbers = {1,2,2,443,23}
print(set_numbers)
#P {1, 2, 443, 23}
set_types = {1,'hola', False ,12.12}
print(set_types)
#P {False, 1, 'hola', 12.12}
set_from_string = set('hola')
print(set_from_string)
#P {'l', 'h', 'a', 'o'}
set_from_tuples = set(('abc','cbv','as','abc'))
print(set_from_tuples)
#P {'abc', 'as', 'cbv'}
numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
#CONVERTIR A FORMATO LISTA LOS NÚMEROS ÚNICOS
unique_numbers = list(set_numbers)