from graphviz import Digraph

class Nodo:
    def __init__(self, str):
        self.str = str
        self.siguiente = None
        self.anterior = None
        self.abajo = None
        
class ListaDOBLE:
    def __init__(self):
        self.primero = None
        self.ultimo = None
         
    #Método que verifica si la lista esta vacía
    def listaVacia(self):
        if self.primero is None:
            return True
        else:
            return False

    #Método agregar MÉTODO FUNCIONAL PARA ENVIAR
    def agregarLista(self, str):
        nuevoNodo = Nodo(str)
        #if type(str) != int:
        try:
            if type(str) != int:
                if self.listaVacia() is True:
                    self.primero = nuevoNodo
                    self.ultimo = nuevoNodo
                    return 0
                else:
                    if self.buscarNodo(str) == 0:
                        if self.primero != None:
                            self.ultimo.siguiente = nuevoNodo
                            nuevoNodo.anterior = self.ultimo
                            self.ultimo = nuevoNodo
                        else:
                            self.primero = nuevoNodo
                            self.ultimo = nuevoNodo
                        return 0
                    elif self.buscarNodo(str) == 2:
                        return 2
                    else:
                        return 1
            else:
                return 1
        except:
            return 1

    #Método Buscar
    def buscarNodo(self, dato):
        actual = self.primero
        encontrado = False
        if self.primero != None:
            while actual != None and encontrado != True:
                if actual.str == dato:
                    encontrado = True
                    return 2
                actual = actual.siguiente
            if not encontrado:
                return 0
        else:
            return 1     

    #Método Eliminar MÉTODO FUNCIONAL PARA ENVIAR
    def eliminarNodo(self, dato):
        aux = self.primero
        tmp = None
        encontrado = False
        try:
            if self.listaVacia() is True:
                return 1
            else:
                if self.primero != None:
                    while aux != None and encontrado != True:
                        if aux.str == dato:
                            if aux == self.primero:
                                self.primero = self.primero.siguiente
                            elif aux == self.ultimo:
                                tmp.siguiente = None
                                self.ultimo = tmp
                            else:
                                tmp.siguiente = aux.siguiente
                                aux.siguiente.anterior = tmp
                            encontrado = True
                            return 0
                        tmp = aux
                        aux = aux.siguiente
                    if not encontrado:
                        return 2
        except:
            return 1

    #Método Modificar MÉTODO FUNCIONAL PARA ENVIAR
    def modificarNodo(self, str, dato):
        try:
            if self.buscarNodo(dato) == 2:

                return 3
            else:
                actual = self.primero
                encontrado = False
                if self.primero != None:
                    while actual != None and encontrado != True:
                        if actual.str == str:
                            encontrado = True
                            actual.str = dato
                            return 0
                        actual = actual.siguiente
                    if not encontrado:
                        return 2
                else:   
                    return 1
        except:
            return 1
        
    #Método imprimir MÉTODO FUNCIONAL PARA ENVIAR
    def imprimir(self):
        lista = []
        tmp = self.primero
        while tmp != None:
            lista.append(tmp.str)
            tmp = tmp.siguiente
        return lista

    #Método Graficar
    def graficar(self, nombre):
        cadena = ""
        cadena2 = ""
        cadena1 = ""
        cadena3 = ""
        cadena4 = ""
        g = Digraph('g', 
            node_attr={'shape': 'record', 'style':'rounded,filled','fillcolor': 'orange:red'})
        g.attr(rankdir='LR')
        g.format = 'png'
        #aquí va todo el codigo que recorre la lista
        #1er while crea los nodos a graficar
        aux = self.primero
        while aux != None:
            cadena = cadena + aux.str
            g.node(cadena,cadena)
            cadena = ""
            aux = aux.siguiente
        #2do while crea los apuntadores siguientes entre nodos 
        tmp = self.primero
        while tmp.siguiente != None:
            cadena2 = cadena2 + tmp.str
            cadena1 = cadena1 + tmp.siguiente.str
            g.edge(cadena2, cadena1)
            cadena1 = ""
            cadena2 = ""
            tmp = tmp.siguiente
        #3er while crea los apuntadores anteriores entre nodos
        tmp = self.ultimo
        while tmp.anterior != None:
            cadena3 = cadena3 + tmp.str
            cadena4 = cadena4 + tmp.anterior.str
            g.edge(cadena3, cadena4)
            cadena3 = ""
            cadena4 = ""
            tmp = tmp.anterior
        #genera el archivo .Dot y una imagen png
        g.render(nombre+'.gv.png', view=True)
        #g.view() metodo de graphviz para generar pdf con la imagen
