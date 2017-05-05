class Car():
    def __init__(self, make, model, year, color='red'):
        self.make = make
        self.model = model
        self.year = year
        self.color = color 
        self.fuel_level = 0
        self.fuel_capacity = 100
        self.new_level = 0
        #__ es para hacerlo privado

    def __str__(self):
        return "Coche: modelo: %s, color: %s" % (self.model, self.color)

    def fill_tank(self):
        """Fill gas tank to capacity."""
        if self.fuel_level == self.fuel_capacity:
            print("Fuel tank is full.")
        else:
            print("No está del todo lleno")

    def update_fuel_level(self, new_level):
        if new_level <= self.fuel_capacity:
            self.fuel_level = new_level
        #else:
            #print("The tank can't hold that much!")
    
    def add_fuel(self, amount):
        if (self.fuel_level + amount <= self.fuel_capacity):
            self.fuel_level += amount
            print("Added fuel.")
        else:
            print("The tank won't hold that much.")

class ElectricCar(Car):
    """A simple model of an electric car."""

    def __init__(self, make, model, year):
        """Initialize an electric car."""
        super().__init__(make, model, year)

        # Attributes specific to electric cars.
        # Battery capacity in kWh.
        self.battery_size = 70
        # Charge level in %.
        self.charge_level = 0

class WareHouse():
    '''almacen de coches'''
    def __init__(self, name):
        self.name = name
        #lista de coches
        self.coches = []

    def add_car(self, coche):
        '''añadimos un coche al almacen'''
        self.coches.append(coche)
        make = input ('Vamos a añadir tu coche, dime el nombre: ')
        model = input ('dime el modelo: ')
        year = input ('dime el año: ')
        print("El coche que has guardado es un: " + make + " " + model + " " + year)

    def rm_car(self, coche):
        '''borramos un coche'''
        self.coches.remove(coche)

""" crear los objetos """
mycar1 = Car('audi','a4','2010', 'green')
mycar2 = Car('bmw','x5','2013', 'yellow')
mycar3 = Car('seat','ibiza','2002', 'blue')
myElectricCar = Car('Tesla', 'S', 2016)

'''creamos el almacen1'''
almacen1 = WareHouse ('al1')
almacen1.add_car(mycar1)
'''imprimo el nombre del almacen'''
print(almacen1.name)

'''vamos a añadir un coche'''
print(almacen1.add_car)

'''imprimo todos los coches del almacen'''
for car in almacen1.coches:
    print(car)


#print("Marca: "+mycar1.make)
#print("Modelo: "+mycar1.model)
#print("Año: "+mycar1.year)

""" modificar atributos """
mycar1.year = 2016
#mycar1.add_fuel(150)
#print(mycar1.year)
#print(mycar1.fill_tank())
#print(mycar1.fuel_level)

''' lista de coches '''
lista_coches = []
lista_coches.append(mycar1)
lista_coches.append(mycar2)

'''print de todos los coches'''
#for coche in lista_coches:
#    print(coche)

'''te imprime la cantidad de coches que hay en la lista'''
#print(str(len(lista_coches)))

'''si hay mas de un coche o si no hay'''
#if len(lista_coches) > 0:
#    print("hay coches")
#else:
#    print("no hay coches")
