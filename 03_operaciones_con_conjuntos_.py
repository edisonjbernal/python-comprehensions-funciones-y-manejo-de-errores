set_a = {'col','mex','bol'}
set_b = {'pe','bol'}

#UNION
set_c = set_a.union(set_b)
print(set_c)
#P {'mex', 'pe', 'bol', 'col'}

#Sintaxis diferente, mismo resultado
print(set_a | set_b)
#P {'mex', 'pe', 'bol', 'col'}

#INTERSECTION
set_c = set_a.intersection(set_b)
print(set_c)
#P {'bol'}

#Sintaxis diferente, mismo resultado
print(set_a & set_b)
#P {'bol'}

#DIFERENCE
set_c = set_a.difference(set_b)
print(set_c)
#P {'mex', 'col'}

#Sintaxis diferente, mismo resultado
print(set_a - set_b)
#P {'mex', 'col'}

#SYMMETRIC DIFERENCE
set_c = set_a.symmetric_difference(set_b)
print(set_c)
#P {'pe', 'col', 'mex'}

#Sintaxis diferente, mismo resultado
# (^) Signo de intercalación
print(set_a ^ set_b)
#P {'pe', 'col', 'mex'}