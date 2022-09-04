from colorama import Fore
from ListaSimpleEnlazada import ListaSimpleEnlazada
from pruebas import pruebas
from Pelicula import Pelicula
import xml.etree.ElementTree as ET


def menu():
    opcion = ''
    listapruebases = ListaSimpleEnlazada()
    while opcion != '8':
        print(Fore.CYAN + "----------------MENU----------------")
        #print(Fore.CYAN + "1 -- CREAR pruebas")
        print(Fore.CYAN + "2 -- IMPRIMIR ANALISIS")
        print(Fore.CYAN + "3 -- BUSCAR pruebas")
        #print(Fore.CYAN + "4 -- AGREGAR PELICULA A pruebas")
        print(Fore.CYAN + "5 -- IMPRIMIR PELICULAS POR pruebas")
        print(Fore.CYAN + "6 -- CARGAR DESDE ARCHIVO")
        print(Fore.CYAN + "8 -- SALIR")


        opcion = input(Fore.YELLOW + "Seleccione una opcion del menu\n")

        if opcion == '1':
            c = input(Fore.BLUE + "Ingrese pruebas en el siguiente formato nombre-edad-nacionalidad\n")
            datos = c.split('-')
            nuevopruebas = pruebas(datos[0], datos[1], datos[2])
            listapruebases.append(nuevopruebas)
            print(Fore.GREEN + "Se registro el pruebas con exito!!\n")
        elif opcion == '2':
            listapruebases.printListaSimpleEnlazada()
        elif opcion == '3':
            nombre = input(Fore.BLUE + "Ingrese el nombre del pruebas\n")
            pruebas = listapruebases.buscarpruebas(nombre)
            if pruebas is None:
                print(Fore.RED + "El pruebas no esta registrado")
            else:
                print(Fore.GREEN +  "(" + pruebas.nombre + " " + pruebas.edad + " " + pruebas.nacionalidad + ")\n" )
        elif opcion == '4':
            nombre = input(Fore.BLUE + "Ingrese el nombre del pruebas\n")
            pruebas = listapruebases.buscarpruebas(nombre)
            if pruebas is None:
                print(Fore.RED + "la pruebas no esta registrado")
            else:
                pelicula = input(Fore.BLUE + "Ingrese pelicula en el siguiente formato nombre-papel-anio-duracion\n")
                datos = pelicula.split('-')
                nuevaPelicula = Pelicula(datos[0],datos[1],datos[2],datos[3])
                pruebas.listaPeliculas.append(nuevaPelicula)
                print(Fore.GREEN + "Se registro pelicula con exito!!\n")
        elif opcion == '5':
            nombre = input(Fore.BLUE + "Ingrese el nombre del pruebas\n")
            pruebas = listapruebases.buscarpruebas(nombre)
            if pruebas is None:
                print(Fore.RED + "El pruebas no esta registrado")
            else:
                pruebas.listaPeliculas.printDobleEnlazada()
        elif opcion == '6':
            nombre = input(Fore.BLUE + "Ingrese el nombre del archivo\n")
            ruta = './' + nombre
            listapruebases = cargaArchivo(ruta)
            print(Fore.GREEN + "Se cargo archivo con exito!!\n")


def cargaArchivo(ruta):
    tree = ET.parse(ruta)
    root = tree.getroot()
    listapruebases = ListaSimpleEnlazada()

    for pruebases in root:
        nuevopruebas = pruebas(pruebases.attrib['nombre'], pruebases.attrib['edad'], pruebases.attrib['nacionalidad'])
        listapruebases.append(nuevopruebas)
        for peliculas in pruebases.iter('pelicula'):
            nuevaPelicula = Pelicula(peliculas.attrib['nombre'],peliculas.attrib['papel'],peliculas.attrib['anio'],peliculas.text )
            nuevopruebas.listaPeliculas.append(nuevaPelicula)
    
    return listapruebases

menu()
        
