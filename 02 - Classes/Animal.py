# CLASE PADRE
class Animal():
    def __init__(self, especie):
        self.especie = especie
        self.nombre = None
        self.patas = 4
    def getEspecie(self):
        return self.especie
    def getPatas(self):
        return self.patas
    def habla(self):
        pass
    def __add__(self, other):
        return self.patas + other.getPatas();



# CLASES HIJAS
class Perro(Animal):
    def __init__(self, nombre):
        super().__init__('Perro')
        self.nombre = nombre
    def habla(self):
        return "wow wow soy un " + super().getEspecie()

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__("Gato")
        self.nombre = nombre
    def habla(self):
        return "miao miao soy un " + super().getEspecie()

class Vaca(Animal):
    def __init__(self, nombre):
        super().__init__('Vaca')
        self.nombre = nombre
    def habla(self):
        return "mooo mooo soy una " + super().getEspecie()

## testing

kitty = Gato('Kitty')
spike = Perro('Spike')
munch = Vaca('Munch')


print(kitty.habla())
print(spike.habla())
print(munch.habla())

print('Kitty y Munch tienen ' + str(kitty + munch) + ' patas')

print('End!')
