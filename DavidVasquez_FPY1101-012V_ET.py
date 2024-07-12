#ExamenTransversal 
import os
import time 
import csv 
import random 


trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
trabajadores_sueldos = {}
sueldos = []
menu = 1
menu2 = 1
seleccion = 0
sueldos_1 = []
sueldos_2 = []
sueldos_3 = []
s = 0

def sueldos_aleatorios (): 
    print ("Asignación de sueldos aleatorios.") 
    for i in range (10): 
        sueldo_aleatorio = random.randint(300000, 2500000)
        sueldos.append (int(sueldo_aleatorio))
    print ("Asignación de sueldos exitosa.")

def clasificacion_sueldos(): 
    for sueldo in sueldos:
                if sueldo < 800000:
                    sueldos_1.append (sueldo)
                    print (f"Sueldos menores a $800.000. TOTAL:{len(sueldos_1)}")
                    print (f"Nombre empleado\t\tSueldo")
                    print (f"{trabajadores[1]}\t\t${sueldos[1]}")

                if 800000 < sueldo < 2000000: 
                    sueldos_2.append (sueldo)
                    print (f"Sueldos entre $800.000 y $2.000.000 TOTAL:{len(sueldos_2)}")
                    print (f"Nombre empleado\t\tSueldo")
                    print (f"{trabajadores[1]}\t\t${sueldos[1]}")
                
                                
                if sueldo > 2000000: 
                    sueldos_3.append(sueldo)
                    print (f"Sueldos superiores a $800.000. TOTAL:{len(sueldos_3)}")
                    print (f"Nombre empleado\t\tSueldo")
                    print (f"{trabajadores[1]}\t\t${sueldos[1]}")

def salir_programa(): 
    s = input("Para salir del programa, presione (s): ")
    print ("Saliendo del programa")
    if s == "s":
        menu = 0
    else: 
        print ("Salida abortada.")

def media_geometrica():
    for valor in sueldos:
        valor *= valor
    return valor ** (1/len(sueldos))

def sueldos_trabajadores():
    trabajadores_sueldos = {
                    "Juan Pérez": sueldos[0],
                    "María García": sueldos[1],
                    "Carlos López": sueldos[2],
                    "Ana Martínez": sueldos[3],
                    "Pedro Rodríguez": sueldos[4],
                    "Laura Hernández": sueldos[5],
                    "Miguel Sánchez":sueldos[6],
                    "Isabel Gómez": sueldos[7],
                    "Francisco Díaz": sueldos[8],
                    "Elena Fernández": sueldos[9]
}
    print (trabajadores_sueldos)

def limpiar_pantalla(): 
     os.system("cls")
    
#def guardar_archivo (): 
     #with open ("archivo.csv", "w", newline= "") as archivo: 
        #archivo.DictWriter (archivo.csv)
    

while menu ==1: 
        print ("-----Menú Sueldos-----")
        print ("1. Asignar sueldos aleatorios")
        print ("2. Clasificar sueldos")
        print ("3. Ver estadísticas.")
        print ("4. Reporte de sueldos")
        print ("5. Salir del programa")
      
        seleccion = int(input("Por favor, seleccione su opción presionando (1/2/3/4/5): "))

        if seleccion == 1:
            limpiar_pantalla() 
            sueldos_aleatorios()
            sueldos_trabajadores()

            time.sleep (3)
            limpiar_pantalla()
                     
        elif seleccion == 2: 
            limpiar_pantalla()
            clasificacion_sueldos ()
           

        
             
        elif seleccion == 3: 
            limpiar_pantalla()
            print ("-----Estadísticas salariales.-----")
            print ("Sueldo más alto:  $", max(sueldos))
            print ("Sueldo más bajo: $", min(sueldos))
            print ("Promedio de sueldos: $", sum(sueldos)/len(sueldos))
            print ("Media geométrica: ", media_geometrica())



        
        #elif seleccion == 4: 
            #print (f"Nombre empleado\t\tSueldo Base\t\tDescuento Salud\t\tDescuento AFP\t\tSueldo Líquido")
            #dcto_salud = sueldos[0]*0.7
            #dcto_afp = sueldos[0]*0.12
            #print (f"{trabajadores[1]}\t\t${sueldos[1]}")
            
        elif seleccion == 5:
            limpiar_pantalla()
            salir_programa()
            break


     
             
            
            

        
             
        

        
             



        








            




















































