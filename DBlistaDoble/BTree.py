class NodeBTree :
    def __init__(self) :
        self.gradeTree = 4
        self.maxKeys = self.gradeTree -1
        self.keys = []
        self.children = []
        self.parentNode = None

class Registro:
    def __init__(self,listRegister):
        self.register = listRegister
        self.idHide = 0

class BTree :
    
    def __init__(self):
        self.root = None
        self.identity = 0
        self.maxColumna = 0
        self.listRegister = []

    def isTreeEmpty(self) :
        if self.root is None:
            return True
        else:
            return False
    
    def searchNodeToInsert(self,currentRegister,currentNode) :
        
        maxKeys = len(currentNode.keys)
        i = 0
        while i <  maxKeys and currentNode.keys[i].register[0] < currentRegister.register[0]:
            i += 1
        if i < maxKeys and currentNode.keys[i].register[0] == currentRegister.register[0]:
            return currentNode.keys[i].register
        if len(currentNode.children) == 0:
            return currentNode
        else: 
            return self.searchNodeToInsert(currentRegister,currentNode.children[i])

    def insertSorted(self,register,currentNode,childNode) :
        pivote = 0
        if len(currentNode.keys) == 0:
            currentNode.keys.append(register)
        else:
            # Encuentra la posicion del valor mayor a el
            while currentNode.keys[pivote].register[0] < register.register[0] :
                pivote += 1
                #desborda el indice
                if pivote > len(currentNode.keys) -1 :
                    break
            currentNode.keys.append(None)
            #desplaza una pos hacia adelante cada clave
            for i in range( len(currentNode.keys) -1, pivote-1 , -1 ):
                currentNode.keys[i] = currentNode.keys[i-1]
            if childNode is not None:
                currentNode.children.append(None)
                #desplaza una pos hacia adelante cada hijo
                for i in range( len(currentNode.children) -1, pivote , -1 ):
                    currentNode.children[i] = currentNode.children[i-1]
                #agrega un nuevo nodo en una pos ordenada del nodo padre
                currentNode.children[pivote+1] = childNode
            #agrega una nueva clave en una pos ordenada
            currentNode.keys[pivote] = register

    def splitCurrentNode(self,nodeToSplit) :
        rightNode = NodeBTree()
        leftNode = NodeBTree()
        print("----------------------------------")
        print("Node to split: ",nodeToSplit.keys)
        print("----------------------------------")
        MINUSCHILDREN = int(((nodeToSplit.gradeTree/2) - 1) + 1)
        for i in range(MINUSCHILDREN,nodeToSplit.gradeTree+1):
            rightNode.keys.append(nodeToSplit.keys[MINUSCHILDREN])
            del nodeToSplit.keys[MINUSCHILDREN]
            if len(nodeToSplit.children) != 0:
                rightNode.children.append(nodeToSplit.children[MINUSCHILDREN+1]) 
                del nodeToSplit.children[MINUSCHILDREN+1]
        newParent = NodeBTree()
        newParent.keys.append(rightNode.keys[0])
        leftNode = nodeToSplit
        rightNode.parentNode = newParent.parentNode
        del rightNode.keys[0]
        print("Left node: ",nodeToSplit.keys,"New parent: ",newParent.keys,"Right node: ",rightNode.keys)    
        if nodeToSplit.parentNode is None:
            self.root = newParent
            leftNode.parentNode = self.root
            rightNode.parentNode = self.root
            print("Parent of left : {} ".format(leftNode.parentNode.keys))
            print("Parent of right : {} ".format(rightNode.parentNode.keys))
            self.root.children.append(leftNode)
            self.root.children.append(rightNode)
        else:
            parent = nodeToSplit.parentNode
            self.insertSorted(newParent.keys[0],parent,rightNode)
            rightNode.parentNode = parent
            print("Parent**left {} ".format(leftNode.parentNode.keys))
            print("**leftKeys {} ".format(leftNode.keys))
            print("**rightKeys {} ".format(rightNode.keys))
            print("Parent**right {} ".format(rightNode.parentNode.keys))
            del newParent
            if len(parent.keys) > parent.gradeTree:
                self.splitCurrentNode(parent)

    def insertSubtree(self,value,currentNode) :
        # Nodo es una hoja o raiz
        if len(currentNode.children) == 0 :
            self.insertSorted(value,currentNode,None)
        else: 
            nodeToInsert = self.searchNodeToInsert(value,currentNode)
            self.insertSubtree(value,nodeToInsert)
        if len(currentNode.keys) > currentNode.gradeTree:
            self.splitCurrentNode(currentNode)
            

    def insertNode(self,currentRegister) :
        self.identity += 1
        currentRegister.idHide = self.identity
        self.listRegister.append(currentRegister)
        print("{} {}".format(currentRegister.idHide,currentRegister.register))
        if self.isTreeEmpty() :
            newNode = NodeBTree()
            newNode.keys.append(currentRegister) 
            self.root = newNode
        else:
            self.insertSubtree(currentRegister,self.root)
    


if __name__ == "__main__":
    miRegister = Registro([33,"Steve","Morales"])
    miRegister2 = Registro([11,"Peter","Morales"])
    miRegister3 = Registro([3,"Ariadna","Samayoa"])
    miRegister4 = Registro([21,"Csterion","Morales"])
    miRegister5 = Registro([4,"Luis","Morales"])
    miRegister6 = Registro([5,"Jaime","Samayoa"])
    miRegister7 = Registro([25,"Brian","Samayoa",25])

    miArbol = BTree()
    miArbol.insertNode(miRegister)
    miArbol.insertNode(miRegister2)
    miArbol.insertNode(miRegister3)
    miArbol.insertNode(miRegister4)
    miArbol.insertNode(miRegister5)
    miArbol.insertNode(miRegister6)
    miArbol.insertNode(miRegister7)
    
    # print(miArbol.listRegister)
    
    print("----------------------------------------------------")
    print("----------------------------------------------------")
    print("ROOT: [{}]".format(miArbol.root.keys[0].register))
    print("----------------------------------------------------")
    print("----------------------------------------------------")
    print("child[0]: {},{},{} ".format(miArbol.root.children[0].keys[0].register,miArbol.root.children[0].keys[1].register,miArbol.root.children[0].keys[2].register))
    print("child[1]: {},{},{}".format(miArbol.root.children[1].keys[0].register,miArbol.root.children[1].keys[1].register,miArbol.root.children[1].keys[2].register))
    for i in range(len(miArbol.root.children)):
        print("child[{}]: {} ".format(i,miArbol.root.children[i].keys))
    
    # print("--------------------------------------------------------")
    # print(miArbol.root.children[0].children[0].keys,miArbol.root.children[0].children[1].keys)
    # print("--------------------------------------------------------")
    # print(miArbol.root.children[1].children[0].keys,miArbol.root.children[1].children[1].keys,miArbol.root.children[1].children[2].keys)


