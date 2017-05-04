class Car():
    def __init__(self, make, model, year, color):
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

""" crear los objetos """
mycar1 = Car('audi','a4','2010', 'green')
mycar2 = Car('bmw','x5','2013', 'yellow')
mycar3 = Car('seat','ibiza','2002', 'blue')

#print("Marca: "+mycar1.make)
#print("Modelo: "+mycar1.model)
#print("Año: "+mycar1.year)

""" modificar atributos """
mycar1.year = 2016
mycar1.add_fuel(150)
#print(mycar1.year)
#print(mycar1.fill_tank())
print(mycar1.fuel_level)