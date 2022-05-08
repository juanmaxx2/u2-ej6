class Viajero():
    __Nombre=""
    __Apellido=""
    __DNI=""
    __num_viajero=int
    __millas_acum=int
    
    def __init__(self,nombre,apellido,dni,num_viajero,millas_acum):
        self.__Nombre=nombre
        self.__Apellido=apellido
        self.__DNI=dni
        self.__num_viajero=num_viajero
        self.__millas_acum=millas_acum
    
    def getNombre(self):
        return self.__Nombre
    
    def getMillas(self):
        return int(self.__millas_acum)
    
    def getNumero(self):
        return self.__num_viajero
    
    def __str__(self):
        return str(self.__num_viajero, self.__millas_acum)
    
    def __gt__(self,other):
        return self.getMillas()<other.getMillas()
    
    def __add__(self,other):
        return self.getMillas()+other.getMillas()
    
    def __sub__(self,other):
        return self.getMillas()-other