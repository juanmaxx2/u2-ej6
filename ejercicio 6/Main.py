import csv
from errno import ELIBBAD
from Viaje import Viajero

if __name__ == '__main__':
    lista=[]
    archivo = open("Viajantes.csv")
    reader=csv.reader(archivo,delimiter=",")
    total=0
    c=0
    for fila in reader:
        objeto=Viajero(fila[0], fila[1], fila[2], int(fila[3]), int(fila[4]))
        lista.append(objeto)
    numero = int(input('\ningrese numero de pasajero:'))
    opcion = None
    for objeto in lista:
        if numero == objeto.numero():
            while opcion!='d':
                print('\n')
                print ('a) Cantidad de millas')
                print ('b) Acumular millas')
                print ('c) Canjear millas')
                print ('d) el viajero que tiene mas millas')
                print ('e) restar millas')
                print ('f) sumar millas')
                print ('g) salir')
                opcion = input('\nIngrese opcion a realizar:')
                
                if opcion == 'a':
                    cantidad=objeto.CantidadTotalMillas()
                    print ('\ncantidad total de millas acumuladas es:', format(cantidad))
                  
                elif opcion == 'b':
                    milla=int(input('\ncantidad de millas que recorridas:'))
                    acum=objeto.AcumularMillas(milla)
                    print('\nla cantidad de millas en total es:', format(acum))
                      
                elif opcion == 'c':
                    cantmi=int(input('\ningrese la cantidad de millas que desesa canjear:'))
                    cant=objeto.CanjearMillas(acum,cantmi)
                  
                elif opcion=='d':
                    objeto.__gt__(lista)
                
                elif opcion=='e':
                    print('la cantidad de millas acumuldas son:',objeto.__add__(lista))
                
                elif opcion=='f':
                    print('la cantidad de millas restadas es:',lista.__sub__(lista))