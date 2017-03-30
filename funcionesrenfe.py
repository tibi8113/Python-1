""" billete """
mizona=1
origen="Irun"
billete=""
destino=""

zonas = {
            1 : ["Irun", "Ventas", "Renteria", "Pasaia"],
            2 : ["Herrera","Intxaurrondo", "Gros", "Donostia"],
            3 : ["Loiola","Martutene", "Urnieta", "Andoain"],
            4 : ["Tolosa","Ordizia", "Ormaiztegi", "Zumarraga"]
        }

precios = {
            "ida": [1.9, 1.95, 2.10, 2.20],
            "i/v": [2.75, 2.90, 3.50, 3.75],
            "mensual": [40, 44, 48, 52]
            }
    
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

def mi_num_zona(zona_dest):
    precios=zona_dest-mizona
    return precios

def mi_precio():
    zonadestino = mi_zona(destino)
    zona = abs(mizona - zonadestino)
    return precios[billete][zona]