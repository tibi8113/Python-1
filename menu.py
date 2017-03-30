import funcionesrenfe as fr


""" menu principal """
precios=0
zona_dest=0
""" imprimo el menu """
print("Que billete desea coger?:")

""" guardo la opcion selecionada """
fr.billete=input("a) ida" + "\n" +" b) ida y vuelta "+ "\n" +" c)mensual "+ "\n")

""" imprimo el tipo de billete que ha seleccionado """
fr.billete_bi(fr.billete)

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
fr.mi_precio()











