
# this is not a good practice in some cases
entrada_1 = 'Nombre'
if entrada_1 == 'Nombre':
    print('Bad practice')
else: 
    print('What')

# this is a good practice
if entrada_1.lower() == 'NOmbre'.lower():
    print('Good Practice')
else:
    print('Not working')


for letter in 'UNIVERSIDAD':
    print(letter)

suma = 0
for i in range(0, 10):
    suma += i
print(suma)

# this second example has an detail... python is not like javascript that concatenates int as strings
# it needs to use str()
suma = ''
for i in range(0, 10):
    suma += str(i)
print(suma)


print('End!')