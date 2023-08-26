set_countries = {'col','mex','bol'}

#Tamaño
size = len(set_countries)
print(size)
#P 3

#Preguntar si cierto elemento está dentro del conjunto.
print('col' in set_countries)
#P True
print('us' in set_countries)
#P False

#add o añadir
set_countries.add('us')
print(set_countries)
#P {'us', 'mex', 'bol', 'col'}

#Update o actualizar

set_countries.update({'us','pe','cl'})
print(set_countries)
#P {'mex', 'pe', 'cl', 'col', 'us', 'bol'}

#Remover pero si no lo encuentra aparece error
set_countries.remove('col')
print(set_countries)
#P {'bol', 'cl', 'mex', 'us', 'pe'}

#Remover pero si no lo encuentra no aparece un error
set_countries.discard('in')
print(set_countries)

#Clear - Limpiar todo el conjunto
set_countries.clear()
print(set_countries)
#P set()