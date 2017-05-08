#HOMEWORK

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-c2f", "--CelToFah", help="Celsius to Fahrenheit", action="store_true")
parser.add_argument("-c2k", "--CelToKel", help="Celsius to Kelvin", action="store_true")
parser.add_argument("-f2c", "--FahToCel", help="Fahrenheit to Celsius", action="store_true")
parser.add_argument("-f2k", "--FahToKel", help="Fahrenheit to Kelvin", action="store_true")
parser.add_argument("-k2c", "--KelToCel", help="Kelvin to Celsius", action="store_true")
parser.add_argument("-k2f", "--KelToFah", help="Kelvin to Fahrenheit", action="store_true")

parser.add_argument("-n", "--number", type=int, help="The number to convert")
args = parser.parse_args()

number = args.number
type = 'NaN'
result = 0

if args.CelToFah:
    type = 'CelToFah'
    result = number * 1.8 + 32

if args.CelToKel:
    type = 'CelToKel'
    result = number + 273.15

if args.FahToCel:
    type = 'FahToCel'
    result = (number - 32) / 1.8

if args.FahToKel:
    type = 'FahToKel'
    result = (number + 459.67) * 5/9

if args.KelToCel:
    type = 'KelToCel'
    result = number - 273.15

if args.KelToFah:
    type = 'KelToFah'
    result = number * 5/9 - 459.67

print('\n\tThe result of {} of the number {} equals to {}'.format(type, number, result))