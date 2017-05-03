class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.__color = 'red' #__ es para hacerlo privado
        self.fuel_level = 0
        self.fuel_capacity = 100

    def fill_tank(self):
        """Fill gas tank to capacity."""
        if self.fuel_level == self.fuel_capacity:
            print("Fuel tank is full.")
        else:
            print("No está del todo lleno")

""" crear los objetos """
mycar1 = Car('audi','a4','2010')
mycar2 = Car('bmw','x5','2013')
mycar3 = Car('seat','ibiza','2002')

#print("Marca: "+mycar1.make)
#print("Modelo: "+mycar1.model)
#print("Año: "+mycar1.year)

""" modificar atributos """
mycar1.year = 2016
#print(mycar1.year)
print(mycar1.fill_tank())