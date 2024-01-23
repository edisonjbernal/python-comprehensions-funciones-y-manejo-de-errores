file = open('text.txt')
#print(file.read())

""" print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='') """

for line in file:
    print(line, end='')



file.close()

# Esto lo cierra automáticamente
with open('text.txt') as file:
    for line in file:
        print(line, end='**')

