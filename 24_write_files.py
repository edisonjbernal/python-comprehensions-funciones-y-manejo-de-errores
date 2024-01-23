# Esto lo cierra automáticamente
#permiso (r+) lee y agrega
#permiso (w+) lee y reemplaza
with open('text.txt','w+') as file:
    for line in file:
        print(line, end='**')
    file.write('Después del final\n')
