import os, sys, time
from listaPacientes import ListaPaciente
import xml.etree.ElementTree as ET

ListaPaciente = ListaPaciente()

def cls():
    os.system("cls")

def cargar(ruta):
    tree = ET.parse(ruta)
    root = tree.getroot()
    for elemento in root:
        print("Paciente: ", elemento.attrib["nombre"], "ha sido insertado")
        #Almaceno el nombre del nodo
        nombre = elemento.attrib["nombre"]

        #Almaceno la datos personales  
        for datoss in elemento.iter("datospersonales"):
            print("Datos del Paciente")
            for columna in datoss.iter("nombre"):
                tamM = columna.text
                print("Nombre del paciente: ", tamM)
            for fila in datoss.iter("edad"):
                tamN = fila.text
                print("Edad del paciente: ", tamN)

        #Almaceno la posicion de inicio del nodo
        for subelemento in elemento.iter("posicioninicio"):
            
            for inicioX in subelemento.iter("x"):
                xInicio = inicioX.text
                
            for inicioY in subelemento.iter("y"):
                yInicio = inicioY.text
                

        #Almaceno la posicion de fin del nodo
        for subelemento in elemento.iter("posicionfin"):
            
            for finx in subelemento.iter("x"):
                xFin = finx.text
             
            for finy in subelemento.iter("y"):
                yFin = finy.text
                

                ListaPaciente.agregarPaciente(nombre, tamM, tamN, xInicio , yInicio, xFin, yFin)

        #Agregamos la matriz a la lista de Pacientes
        for subelemento in elemento.iter("celda"):
            print("f=", subelemento.attrib['f'], " c=",  subelemento.attrib['c'])
            Paciente = ListaPaciente.buscarPaciente(elemento.attrib["nombre"])
            Paciente.matriz.insertar(subelemento.attrib['f'], subelemento.attrib['c'], subelemento.text)
            



def menu():
    cls()
    while True:
        print("""\n          ***   Menú Principal   ***\n          
        1. Cargar archivo
        2. Procesar archivo
        3. Generar archivo salida
        4. Creditos
        5. Generar gráfica
        6. Salir""")

        opc = input("\nOpción a realizar: ")

        if opc == "1": 
            cls()
            print("   --- Cargar Archivo ---   \n")
            try:
                archivo = input("Ingrese el nombre del archivo\n")
                Filename = './' + archivo
                cargar(Filename)
                input("\n--> Archivo cargado exitosamente...")
                cls()
                menu()
            except:
                input("El nombre del archivo no se ha encontrado...")
                menu()
            break
        elif opc == "2":
            cls()
            input("--> Listado de Pacientes agregados: \n")
            ListaPaciente.mostrarPacientes()
            input()
            menu()
            break
        elif opc == "3":
            cls()
            nombre = input("Ingrese el nombre del Paciente: \n")
            Paciente = ListaPaciente.buscarPaciente(nombre)

            if Paciente == None:
                input("Paciente no ingresado aun...")
            else:
                print("Paciente: ", Paciente.nombre)
                Paciente.matriz.recorrerFilas()
                input()
                Paciente.matriz.imagenDot()
                Paciente.matriz.reporte(nombre)
                input("Presione una tecla para continuar")
            
            menu()
            break
        elif opc == "4":
            cls()      
            print("\n                 Creditos                   \n")     
            print("**********************************************")
            print("****                IPC 2 N               ****")
            print("****    Henry Alexander García Montúfar   ****")
            print("****              201407049               ****")
            print("**********************************************\n")

            input("Presione una tecla para continuar...")
            menu()
            break
        elif opc == "5":
            cls()
            nombre = input("Ingrese el nombre del Paciente: \n")
            nombre = "1"
            Paciente = ListaPaciente.buscarPaciente(nombre)

            if Paciente == None:
                input("Paciente no ingresado aun...")
            else:
                print("Paciente: ", Paciente.nombre)
                Paciente.matriz.recorrerFilas()
                print("Imagen generada...\n")
                Paciente.matriz.reporte(nombre)
                input("Presione para continuar")
        elif opc == "6":
            cls()
            print("Saliendo del sistema...")
            time.sleep(0.5)
            os.system("exit")
            break

menu()

