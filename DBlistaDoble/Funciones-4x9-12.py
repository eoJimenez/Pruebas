from listaDoble import *
#import claseBD
#import claseArbolB
import os

class nodo :
    def __init__(self,nombreDeLaTabla,numeroDeColumnasDeLaTabla) :
    #def __init__(self,nombreDeLaTabla,numeroDeColumnasDeLaTabla,listaDeElementosDeLaTabla) : #descomentar si es necesario
        self.nombre = nombreDeLaTabla
        self.columnas = numeroDeColumnasDeLaTabla
        #self.elementos = listaDeElementosDeLaTabla
        self.siguiente = None
        self.anterior = None

class ListaDobledeArboles :
    
    def __init__ (self) :
        self.inicio = None
        self.fin = None

    #Metodo para saber si la lista esta vacia
    def estaVacia(self) :
        return self.inicio is None

    #Metodo para buscar una tabla
    def buscarTabla(self,nombreTabla) :
        aux = self.inicio
        while aux != None :
            if aux.nombre == nombreTabla :
                #print("La tabla existe")
                return True
            aux = aux.siguiente
        #print("La tabla no existe")
        return False

    #Metodo para listar los nodos
    def verNodos(self) :
        aux = self.inicio
        while aux != None :
            print(aux.nombre)
            aux = aux.siguiente

    def insertar(self,nombreTabla,numCol) :
        nuevo = nodo(nombreTabla,numCol)
        # lista vacia
        if self.inicio == None :
            self.inicio=self.fin=nuevo
        else:
            self.fin.siguiente = nuevo
            nuevo.anterior = self.fin
            self.fin = nuevo
        return self.inicio

    def eliminar(self,nombreTabla) :
        if self.estaVacia() != None :
            aux = self.inicio
            while aux != None :
                if aux.nombre == nombreTabla :
                    if aux.anterior == None and aux.siguiente == None :
                        self.inicio=self.fin=None
                        return 0
                    #en el original no tenias los elif
                    elif aux.anterior == None :
                        self.inicio = self.inicio.siguiente
                        self.inicio.anterior = None
                        aux.siguiente = None
                        return 0
                    elif aux.siguiente == None :
                        self.fin = self.fin.anterior
                        self.fin.siguiente = None
                        aux.anterior = None
                        return 0
                    else:
                        aux.anterior.siguiente = aux.siguiente
                        aux.siguiente.anterior = aux.anterior
                        aux.anterior = None
                        aux.siguiente = None
                        return 0
                else:
                    aux = aux.siguiente
        else:
            print("No existen tablas")
            #return("BD vacia")
            #return(4)

    def modificar(self,nombreViejo,nombreNuevo):
        aux = self.inicio
        while aux != None :
            if aux.nombre == nombreViejo :
                aux.nombre = nombreNuevo
                return 0
            aux = aux.siguiente

    def graficar(self):
        f = open("listadoble.dot", "w")            
        f.write("digraph G {\n")
        f.write("node [shape = rect, width=1, height=0.4];\n")     
        f.write("rankdir=LR;\n")  
        
        n=self.inicio
        while (n.siguiente!=None):
            #la linea siguiente es para mostrar el nombre de la tabla por separadao, por el momento no es necesario
            #f.write(str(n.nombre)+"[label="+"\""+str.(n.nombre)+"\""+"];")
            f.write("\""+str(n.nombre)+"\"->"+"\""+str(n.siguiente.nombre)+"\";\n")
            f.write("\n")
            n=n.siguiente

        n=self.fin
        while n.anterior!=None :
            f.write("\""+str(n.nombre)+"\"->"+"\""+str(n.anterior.nombre)+"\";\n")
            f.write("\n")
            n=n.anterior

        f.write("}")
        f.close()
        os.system("dot -Tjpg listadoble.dot -o listadoble.png")


#Funcion 1 - crear tabla
# def createTable(database: str, table: str, numberColumns: int) -> int:    
    def createTable(self,database,table,numberColumns) :
        #print(e)
        bdEncontrada  = ""
        bdEncontrada=e.buscarNodo(database)
        if bdEncontrada != None :                                            
            if self.buscarTabla(table) == False :
                #BD encontrada.tablas=table
                bdEncontrada.tabla = self.insertar(table,numberColumns)
                if bdEncontrada.tabla!=None :

                    #return ("Operacion exitosa")
                    return (0)
                else:
                    #return ("Error en la operacion")
                    return (1)
            else:
                #return ("Tabla existente")
                return (3)
        else:                                                                      
            #return ("BD inexistente")
            return (2)                                                             

#Funcion 2 - mostrar tablas
# def showTables(database: str) -> list:                    
    def showTables(self,database) :
        tablas = []
        ed = ListaDOBLE()
        if ed.buscarNodo(database) == 2 :                                             
            if self.estaVacia() != None :
                #devuelve la lista con los nombres de las tablas
                aux = self.inicio
                while aux != None :
                    tablas.append(aux.nombre)
                    aux = aux.siguiente       
            else:
                return tablas
        else:                                                                    
            return None                                                           

#Funcion 3 - mostrar el contenido de la tabla
# def extractTable(database: str, table: str) -> list:

#Funcion 4 - muestra un determinado numero de elementos de la tabla
# def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:

#Funcion 9 - cambiar nombre a la tabla
# def alterTable(database: str, tableOld: str, tableNew: str) -> int:  
    def alterTable(self,database,tableOld,tableNew) :
        ed = ListaDOBLE()
        if ed.buscarNodo(database) == 2 :                                           
            if self.buscarTabla(tableNew) == False :
                if self.buscarTabla(tableOld) == True :
                    r = self.modificar(tableOld,tableNew)
                    if r==0 :
                        #return ("Operacion exitosa")
                        return (0)
                    else:
                        #return ("Error en la operacion")
                        return (1)
                else:
                    #return("tableOld no existente")
                    return(3)
            else:
                #return("tableNew existente")
                return(4)
        else:                                                                     
            #return ("BD inexistente")
            return (2)                                                            


#Funcion 10 - agregar columna
# def alterAddColumn(database: str, table: str, default: any) -> int:

#Funcion 11 - eliminar columna
# def alterDropColumn(database: str, table: str, columnNumber: int) -> int:

#Funcion 12 - eliminar tabla
# def dropTable(database: str, table: str) -> int:           
    def dropTable(self,database,table) :
        ed = ListaDOBLE()
        if ed.buscarNodo(database) == 2 : 
            if self.buscarTabla(table) == True :
                r = self.eliminar(table)
                if r==0 :
                    #return ("Operacion exitosa")
                    return (0)
                else:
                    #return ("Error en la operacion")
                    return (1)
            else:
                #return ("Tabla inexistente")
                return (3) 
        else:                                                                    
            #return ("BD inexistente")
            return (2) 


if __name__ == "__main__":
    print("\n")
    #Pruebas de BD
    e=ListaDOBLE()
    e.agregarLista("bd1")
    e.agregarLista("bd4")
    e.agregarLista("bd2")
    e.agregarLista("bd3")
    print(e.imprimir())


    
    #Pruebas de lista de tablas
    p = ListaDobledeArboles()
    pp  = ListaDobledeArboles()
    
    p.createTable("bd1","tabla1",4)
    p.createTable("bd4","tabla2",9)
    p.createTable("bd1","tabla4",6)
    p.verNodos()

    #print(e.primero.tabla.nombre,e.primero.tabla.siguiente.nombre)
    #print(e.primero.siguiente.tabla.nombre)
    
    '''
    
    p.createTable("bd4","tabla3",4)
    p.createTable("bd1","tabla9",5)

    #p.showTables("bd1")

    #print("\n")
    p.alterTable("bd1","tabla4","tabla200")
    p.verNodos()

    #print("\n")
    #p.dropTable("bd1","tabla3")
    #p.verNodos()

    #p.graficar()
'''
   # print("\n termino")