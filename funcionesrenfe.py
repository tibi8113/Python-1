""" billete """
mizona=1
origen="Irun"
billete=""


zonas = {
            1 : ["Irun", "Ventas", "Renteria", "Pasaia"],
            2 : ["Herrera","Intxaurrondo", "Gros", "Donostia"],
            3 : ["Loiola","Martutene", "Urnieta", "Andoain"],
            4 : ["Tolosa","Ordizia", "Ormaiztegi", "Zumarraga"]
        }


precios = {"ida": [1.9, 1.95, 2.10, 2.20],
            "i/v": [2.75, 2.90, 3.50, 3.75],
            "mensual": [40, 44, 48, 52]}

def imprimir():
    print("Que billete desea coger?:")


def billete_bi(billete):
    if billete == "a":
        print("Has seleccionado ida")
    elif billete == "b":
        print("Has seleccionado ida y vuelta")
    elif billete == "c":
        print("Has seleccionado mensual")
    else:
        print("Error")

def print_zonas():
    for z, v in zonas.items():
        print(v)

""" z zonas, p todo el array de los pueblos, d cada destino """
def mi_zona(destino):
    for z, p in zonas.items():
        for d in p:
            if d == destino:
                zona_dest = z
    return zona_dest

def mi_precio(zona_dest):
    precios=zona_dest-mizona
    print(precios)












""" jdjjdjdjd

def valor(destinos):
    if billete=="a":
        if destinos=="Renteria":
            print("Su billete cuesta 1,50 euros")
        elif destinos=="Herrera":
            print("Su billete cuesta 1,80 euros")
        elif destinos=="Intxaurrondo":
            print("Su billete cuesta 2 euros")
        elif destinos=="Donostia":
            print("Su billete cuesta 2,15 euros")
        elif destinos=="Andoain":
            print("Su billete cuesta 2,30 euros")
        else:
            print("Error")


def valor_iv():
    if billete=="b":
        if destinos=="Renteria":
            print("Su billete cuesta 3 euros")
        elif destinos=="Herrera":
            print("Su billete cuesta 3,60 euros")
        elif destinos=="Intxaurrondo":
            print("Su billete cuesta 4 euros")
        elif destinos=="Donostia":
            print("Su billete cuesta 4,30 euros")
        elif destinos=="Andoain":
            print("Su billete cuesta 4,60 euros")
        else:
            print("Error")

def valor_men():
    if billete=="c":
        if destinos=="Renteria":
            print("Su billete cuesta 40 euros")
        elif destinos=="Herrera":
            print("Su billete cuesta 42 euros")
        elif destinos=="Intxaurrondo":
            print("Su billete cuesta 44 euros")
        elif destinos=="Donostia":
            print("Su billete cuesta 46 euros")
        elif destinos=="Andoain":
            print("Su billete cuesta 48 euros")
        else:
            print("Error") """