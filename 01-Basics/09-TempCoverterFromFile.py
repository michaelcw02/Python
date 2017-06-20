#   Homework 2
#   Michael Chen W.
#   https://github.com/michaelcw02/Python
import os
import random

def CelToFah(number):
    return round(number * 1.8 + 32, 2)

def CelToKel(number):
    return round(number + 273.15, 2)

path = '09-TempCoverterFromFile/'
if not os.path.exists(path + 'lista_temperaturas_en_Celsius.txt'):
    text = open(path + 'lista_temperaturas_en_Celsius.txt', 'w')
    for i in range(0, 30):
        text.write(str(random.randint(-45, 45)) + '\n')
    text.close()

inline = open(path + 'lista_temperaturas_en_Celsius.txt', 'r')
outfile = open(path + 'lista_temperaturas_convertidas.txt', 'w')

for line in inline:
    output = 'Valor_Celsius:Valor_Fahrenheit:Valor_Kelvin\n'
    number = int(line)
    output += str(number) + ' : ' + str(CelToFah(number)) + ' : ' + str(CelToKel(number)) + '\n'
    outfile.write(output)

inline.close()
outfile.close()

print('End!')