'''
Una lista enlazada es una estructura de datos que consiste en una secuencia de nodos, en los que cada nodo está enlazado al siguiente.
Se utiliza para representar listas o colas de datos de longitud variable.

Una lista enlazada simple es una lista enlazada en la que cada nodo tiene un único enlace al siguiente nodo.

Todos los elementos almacenados son de un mismo tipo de dato.

Cada elemento de la lista apunta al siguiente elemento de la lista, excepto el último que apunta a None.

Cada elemento de la lista tiene un predecesor, excepto el primero que no tiene predecesor.

Son objetos y están compuesta por nodos.

Una lista es como un tren formada por vagones, donde cada vagón es un nodo y cada nodo tiene un dato y un puntero al siguiente nodo.
'''

class Nodo(): # Nodo de la lista enlazada
    def __init__(self,dato=None,prox=None): # Constructor de la clase
        self.dato=dato # dato del nodo
        self.prox=prox # Puntero al siguiente nodo
    def __str__(self): # Devuelve una cadena con el dato del nodo
        return str(self.dato)

class Lista(): # Lista enlazada
    def __init__(self): # Constructor de la clase
        self.head=None
        self.len=0 # Longitud de la lista
    
    def insertarinicio(self,dato): # Agrega un elemento al inicio de la lista
        nodo=Nodo(dato) # Crea un nuevo nodo
        nodo.prox=self.head # El nodo siguiente del nuevo nodo es el nodo inicial
        self.head=nodo # El nodo inicial es el nuevo nodo
        self.len+=1 # Incrementa la longitud de la lista

    def append(self,dato): # Agrega un elemento al final de la lista
        nodo=Nodo(dato) # Crea un nuevo nodo
        if self.head==None: # Si la lista está vacía
            self.head=nodo # El nodo inicial es el nuevo nodo
        else: # Si la lista no está vacía
            act=self.head # Crea un nodo auxiliar
            while act.prox!=None: # Recorre la lista hasta el último nodo
                act=act.prox # Avanza al siguiente nodo
            act.prox=nodo # El nodo siguiente del último nodo es el nuevo nodo
        self.len+=1 # Incrementa la longitud de la lista

    def pop (self): # Elimina el último elemento de la lista
        if self.head==None: # Si la lista está vacía
            print("Lista vacía") # Muestra un mensaje de error
        elif self.head.prox==None: # Si la lista tiene un solo elemento
            self.head=None # El nodo inicial es None
            self.len-=1 # Decrementa la longitud de la lista
        else: # Si la lista tiene más de un elemento
            act=self.head # Crea un nodo auxiliar
            while act.prox.prox!=None: # Recorre la lista hasta el penúltimo nodo
                act=act.prox # Avanza al siguiente nodo
            act.prox=None # El nodo siguiente del penúltimo nodo es None
            self.len-=1 # Decrementa la longitud de la lista    

    def insertar(self,dato,pos): # Inserta un elemento en la posición indicada
        if pos<=self.len: # Si la posición es válida
            nodo=Nodo(dato) # Crea un nuevo nodo
            act=self.head # Crea un nodo auxiliar
            if pos==0: # Si la posición es la primera
                nodo.prox=self.head # El nodo siguiente del nuevo nodo es el nodo inicial
                self.head=nodo # El nodo inicial es el nuevo nodo
            else: # Si la posición no es la primera
                for i in range(1,pos): # Recorre la lista hasta la posición anterior a la indicada
                    act=act.prox # Avanza al siguiente nodo
                nodo.prox=act.prox # El nodo siguiente del nuevo nodo es el nodo siguiente del nodo actual
                act.prox=nodo # El nodo siguiente del nodo actual es el nuevo nodo
            self.len+=1 # Incrementa la longitud de la lista
        else:
            print("Posición inválida") # Si la posición no es válida, muestra un mensaje de error
    
    def eliminar(self,pos): # Elimina un elemento de la posición indicada
        if pos<self.len: # Si la posición es válida
            if pos==0: # Si la posición es la primera
                self.head=self.head.prox # El nodo inicial es el nodo siguiente del nodo inicial
            else: # Si la posición no es la primera
                act=self.head # Crea un nodo auxiliar
                for i in range(1,pos): # Recorre la lista hasta la posición anterior a la indicada
                    act=act.prox # Avanza al siguiente nodo
                act.prox=act.sig.prox # El nodo siguiente del nodo actual es el nodo siguiente del nodo siguiente del nodo actual
            self.len-=1 # Decrementa la longitud de la lista
        else:
            print("Posición inválida")
    
    def mostrar(self): # Muestra los elementos de la lista
        act=self.head # Crea un nodo auxiliar
        for i in range(self.len): # Recorre la lista
            print(act.dato) # Muestra el dato del nodo actual
            act=act.prox # Avanza al siguiente nodo
    
    def buscar(self,dato): # Busca un elemento en la lista
        act=self.head # Crea un nodo auxiliar
        for i in range(self.len): # Recorre la lista
            if act.dato==dato: # Si el dato del nodo actual es el buscado
                return i # Devuelve la posición del nodo actual
            act=act.prox # Avanza al siguiente nodo
        return -1 # Si no se encuentra el dato, devuelve -1
    
    def obtener(self,pos): # Obtiene el dato de un elemento de la lista
        if pos<self.len: # Si la posición es válida
            act=self.head # Crea un nodo auxiliar
            for i in range(pos): # Recorre la lista hasta la posición indicada
                act=act.prox # Avanza al siguiente nodo
            return act.dato # Devuelve el dato del nodo actual
        else:
            print("Posición inválida")
            return None
    
    def modificar(self,dato,pos): # Modifica el dato de un elemento de la lista
        if pos<self.len: # Si la posición es válida
            act=self.head # Crea un nodo auxiliar
            for i in range(pos): # Recorre la lista hasta la posición indicada
                act=act.prox # Avanza al siguiente nodo
            act.dato=dato # Modifica el dato del nodo actual
        else:
            print("Posición inválida")
    
    def intercambiar(self,pos1,pos2): # Intercambia dos elementos de la lista
        if pos1<self.len and pos2<self.len: # Si las posiciones son válidas
            act1=self.head # Crea un nodo auxiliar
            for i in range(pos1): # Recorre la lista hasta la posición indicada
                act1=act1.prox # Avanza al siguiente nodo
            act2=self.head # Crea un nodo auxiliar
            for i in range(pos2): # Recorre la lista hasta la posición indicada
                act2=act2.prox # Avanza al siguiente nodo
            aux=act1.dato # Guarda el dato del nodo actual
            act1.dato=act2.dato # Modifica el dato del nodo actual
            act2.dato=aux # Modifica el dato del nodo actual
        else:
            print("Posición inválida")
    
    def ordenar(self): # Ordena los elementos de la lista
        for i in range(self.len-1): # Recorre la lista
            for j in range(i+1,self.len): # Recorre la lista
                if self.obtener(i)>self.obtener(j): # Si el dato del nodo actual es mayor que el dato del nodo siguiente
                    self.intercambiar(i,j) # Intercambia los datoes de los nodos
    
    def invertir(self): # Invierte los elementos de la lista
        for i in range(self.len//2): # Recorre la lista hasta la mitad
            self.intercambiar(i,self.len-i-1) # Intercambia los datoes de los nodos
        
    def vacia(self): # Devuelve True si la lista está vacía
        return self.len==0
    
    def longitud(self): # Devuelve la longitud de la lista
        return self.len
    
    def limpiar(self): # Elimina todos los elementos de la lista
        self.head=None
        self.len=0
    
    def clonar(self): # Devuelve una copia de la lista
        nueva=Lista() # Crea una nueva lista
        act=self.head # Crea un nodo auxiliar
        for i in range(self.len): # Recorre la lista
            nueva.insertar(act.dato,i) # Inserta el dato del nodo actual en la nueva lista
            act=act.prox # Avanza al siguiente nodo
        return nueva # Devuelve la nueva lista
    
    def __del__(self): # Destructor de la clase
        self.limpiar() # Elimina todos los elementos de la lista
    
    def __str__(self): # Devuelve una cadena con los elementos de la lista
        cadena=""
        act=self.head # Crea un nodo auxiliar
        for i in range(self.len): # Recorre la lista
            cadena+=str(act.dato)+" " # Agrega el dato del nodo actual a la cadena
            act=act.prox # Avanza al siguiente nodo
        if cadena == "": # Si la cadena está vacía
            cadena = "Lista vacía"
        return cadena # Devuelve la cadena
    
    def __len__(self): # Devuelve la longitud de la lista
        return self.len
    
    def __getitem__(self,pos): # Devuelve el dato de un elemento de la lista
        return self.obtener(pos)
    
    def __setitem__(self,pos,dato): # Modifica el dato de un elemento de la lista
        self.modificar(dato,pos)
    
    def __eq__(self,otra): # Devuelve True si las listas son iguales
        if self.len==otra.len: # Si los longituds de las listas son iguales
            act1=self.head # Crea un nodo auxiliar
            act2=otra.head # Crea un nodo auxiliar
            for i in range(self.len): # Recorre la lista
                if act1.dato!=act2.dato: # Si los datoes de los nodos actuales son distintos
                    return False # Devuelve False
                act1=act1.prox # Avanza al siguiente nodo
                act2=act2.prox # Avanza al siguiente nodo
            return True # Devuelve True
        else:
            return False
    
    def __ne__(self,otra): # Devuelve True si las listas son distintas
        return not self==otra
    
    def __lt__(self,otra): # Devuelve True si la lista es menor que la otra
        if self.len<otra.len: # Si la longitud de la lista es menor que el de la otra
            return True # Devuelve True
        elif self.len==otra.len: # Si la longitud de la lista es igual que el de la otra
            act1=self.head # Crea un nodo auxiliar
            act2=otra.head # Crea un nodo auxiliar
            for i in range(self.len): # Recorre la lista
                if act1.dato>act2.dato: # Si el dato del nodo actual es mayor que el dato del nodo actual de la otra lista
                    return False # Devuelve False
                act1=act1.prox # Avanza al siguiente nodo
                act2=act2.prox # Avanza al siguiente nodo
            return True # Devuelve True
        else:
            return False
    
    def __le__(self,otra): # Devuelve True si la lista es menor o igual que la otra
        return self<otra or self==otra
    
    def __gt__(self,otra): # Devuelve True si la lista es mayor que la otra
        return not self<=otra
    
    def __ge__(self,otra): # Devuelve True si la lista es mayor o igual que la otra
        return not self<otra

lista=Lista()

lista.append(1)
lista.append(2)

print(lista)