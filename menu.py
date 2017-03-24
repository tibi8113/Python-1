import funcionesrenfe as fr


""" menu principal """

zona_dest=0
""" imprimo el menu """
fr.imprimir()

""" guardo la opcion selecionada """
billete=input("a) ida" + "\n" +" b) ida y vuelta "+ "\n" +" c)mensual "+ "\n")

""" imprimo el tipo de billete que ha seleccionado """
fr.billete_bi(billete)

""" muestro los destinos """
fr.print_zonas()

""" guardo el destino seleccionado """
destino=input("Elija su destino: ")

print("Ha elegido: "+destino+"\n")

""" zona """
zona_dest = fr.mi_zona(destino)
print(zona_dest)

""" precio """
fr.mi_precio(zona_dest)











