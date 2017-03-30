import funcionesrenfe as fr


""" menu principal """
precios=0
zona_dest=0
""" imprimo el menu """
print("Que billete desea coger?:")

""" guardo la opcion selecionada """
b = input("a) ida" + "\n" +" b) ida y vuelta "+ "\n" +" c)mensual "+ "\n")

if b == "a":
    fr.billete="ida"
    print("Has seleccionado ida")
elif b == "b":
    fr.billete="i/v"
    print("Has seleccionado ida y vuelta")
elif b == "c":
    fr.billete="mensual"
    print("Has seleccionado mensual")
else:
    print("Error")


""" muestro los destinos """
fr.print_zonas()

""" guardo el destino seleccionado """
fr.destino=input("Elija su destino: ")

print("Ha elegido: "+fr.destino+"\n")

""" zona """
zona_dest = fr.mi_zona(fr.destino)
print(zona_dest)

""" zona numero """
fr.mi_num_zona(zona_dest)

"""precio"""
print("El precio es: " + str(fr.mi_precio()))











