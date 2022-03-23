class Node(object):
    def __init__(self, father=None, value1=None, value2=None, previous=None, next=None):
        self.father    = father
        self.value1    = value1
        self.value2    = value2
        self.previous  = previous
        self.next   = next

class lista(object):
    head = None
    tail = None

    # INSERT AT THE BEGINNING OF THE LIST
    def insertFirst(self, v1, v2, p):
        new_node = Node(p, v1, v2, None, None)
        if self.head == None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    # INSERT AT THE END OF THE LIST
    def insertLast(self, v1, v2, p):

        new_node = Node(p, v1, v2, None, None)

        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.previous   = self.tail
        self.tail = new_node

    # REMOVE AT THE BEGINNING OF THE LIST
    def deleteFirst(self):
        if self.head is None:
            return None
        else:
            no = self.head
            self.head = self.head.next
            if self.head is not None:
                self.head.previous = None
            else:
                self.tail = None
            return node

    # REMOVE AT THE END OF THE LIST
    def deleteLast(self):
        if self.tail is None:
            return None
        else:
            node = self.tail
            self.tail = self.tail.previous
            if self.tail is not None:
                self.tail.next = None
            else:
                self.head = None
            return node

    def first(self):
        return self.head
    
    def last(self):
        return self.tail

    def empty(self):
        if self.head is None:
            return True
        else:
            return False
        
    def showList(self):
        
        aux = self.head
        str = []
        while aux != None:
            temp = []
            temp.append(aux.value1)
            temp.append(aux.value2)
            str.append(temp)
            aux = aux.next
        
        return str
    
    def showway(self):
        
        current = self.tail
        way = []
        while current.father is not None:
            way.append(current.value1)
            current = current.father
        way.append(current.value1)
        way = way[::-1]
        return way
    
    def showway1(self,value):
                
        current = self.head
        while current.value1 != value:
            current = current.next
    
        way = []
        current = current.father
        while current.father is not None:
            way.append(current.value1)
            current = current.father
        way.append(current.value1)
        return way