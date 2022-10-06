from empresas import empresa
from escritorios import escritorios
from ptsatencion import ptsatencion
from listaclientes import clientes
from listae import listaEmpresa
from listad import listad
from listap import listap
from colorama import Fore
import xml.etree.ElementTree as ET


def menu():
        opcion='' 

        E=listaEmpresa()

        while opcion != '8':
            print(Fore.GREEN + "-----------------MENU---------------")
            print(Fore.CYAN + "1 --- CARGAR EMPRESAS")
            print(Fore.YELLOW + "2 --- IMPRIMIR EMPRESAS")
            print(Fore.RED + "3 --- CARGAR PUNTOS DE ATENCION")
            print(Fore.BLUE + "4 --- MOSTRAR PPUNTOS DE ATENCION")
            print(Fore.GREEN + "5 --- MOSTRAR ESCRITORIOS")
            print(Fore.YELLOW + "6 --- GRAFICAR LISTA DE EMPRESAS")
            print(Fore.CYAN + "8 --- SALIR")

            opcion = input(Fore.LIGHTCYAN_EX + "Seleccione una opcion  del menú \n")

            if opcion == '1':
                nombrearchivo = input(Fore.GREEN + "Ingrese el archivo XML \n")
                ruta = './' + nombrearchivo
                E = cargaArchivo(ruta)
                print(Fore.GREEN + "Se cargo el archivo de manera exitosa!!\n")
            elif opcion == '2':
                E.print()

def cargaArchivo(ruta):
        tree = ET.parse(ruta)
        empresa = tree.getroot()
        listaEmpresasDesdeXml = listaEmpresa()
        for empresaXml in empresa:
            nuevaempresa = empresa(empresaXml.attrib['empresa'], empresaXml.attrib['nombre'], empresaXml.attrib['abreviatura'])
            listaEmpresasDesdeXml.append(nuevaempresa)
            for puntoAtencionXml in empresaXml.iter('puntoAtencion'):
                nuevopuntoAtencion = ptsatencion(puntoAtencionXml.attrib['puntoAtencion'], puntoAtencionXml.attrib['nombre'], puntoAtencionXml.attrib['direccion'], puntoAtencionXml.text )
                nuevaempresa.puntoAtencion.append(nuevopuntoAtencion) 
        return  listaEmpresasDesdeXml 



menu()





            
        