# Class
# Michael Chen Wang
# https://github.com/michaelcw02/Python

#iterates var from 0 to 100 and inserts those that are true to the condition.
a = [var for var in range(0, 100) if var%2]
print(1, a)

b = 'HOLA'

lista = ['alberto', 'carlos', 'alex', 'esteban', b]
otraLista = [var for var in lista if var[0]=='a' or var == 'HOLA']
print(2, lista)
print(3, otraLista)

def foo(a, b, c = None):
    if (c == None):
        return a + b
    return a + b + c

print (4, str(foo(1, 2)))
print (5, str(foo(1, 2, 3)))

valor = 'valor'
def faa(valor):
    valor = 'valorcito'
print(6, valor)


lol = 5
lal = lol
lol = 10
print(7, lal)


la_funcion = foo
print(8, str(la_funcion(3, 4)))


print('End!')