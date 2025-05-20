class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def print_linkedlist(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next  
ll = Linkedlist()
p1 = node(10)
p2 = node(20)
p3 = node(30)
p4 = node(40)
ll.head = p1
p1.next = p2
p2.next = p3
p3.next = p4
ll.print_linkedlist()

# ADDING AN ELEMENT TO THE LINKED LIST
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def printlinkedlist(self):
        curr=self.head
        while(curr!=None):
            print(curr.data)
            curr=curr.next 
    def add(self,e):
        temp=node(e)      
        if(self.head==None):
            self.head=temp
        else:
            curr=self.head
            while(curr.next!=None):
                curr=curr.next
            curr.next=temp         
ll=Linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)
ll.printlinkedlist()

# adding element at the 1st position
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def printlinkedlist(self):
        curr=self.head
        while(curr!=None):
            print(curr.data)
            curr=curr.next 
    def add(self,e):
        temp=node(e)      
        if(self.head==None):
            self.head=temp
        else:
            curr=self.head
            while(curr.next!=None):
                curr=curr.next
            curr.next=temp     
    def add_first(self,e):
        temp=node(e)
        if(self.head==None):
            self.head=temp
        else:
            temp.next=self.head
            self.head=temp                
ll=Linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)
ll.add_first(5)
ll.printlinkedlist()

# ADDING AN ELEMENT AT PARTICULAR INDEX
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def printlinkedlist(self):
        curr=self.head
        while(curr!=None):
            print(curr.data)
            curr=curr.next 
    def add(self,e):
        temp=node(e)      
        if(self.head==None):
            self.head=temp
        else:
            curr=self.head
            while(curr.next!=None):
                curr=curr.next
            curr.next=temp     
    def add_first(self,e):
        temp=node(e)
        if(self.head==None):
            self.head=temp
        else:
            temp.next=self.head
            self.head=temp       
    def add_elemenet_st(self,index,element):
        try:
            if(index==0):
                self.add_first(element)
            else:
                temp=node(element)
                count=0
                curr=self.head
                while(count<index-1):
                    curr=curr.next
                    count=count+1
                temp.next=curr.next
                curr.next=temp
        except AttributeError:
            raise IndexError('index'+str(index)+'does not exist')                                
ll=Linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)
ll.add_elemenet_st(10,100)
ll.printlinkedlist()

# add all(adding multiple elements)
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def printlinkedlist(self):
        curr=self.head
        while(curr!=None):
            print(curr.data)
            curr=curr.next 
    def add(self,e):
        temp=node(e)      
        if(self.head==None):
            self.head=temp
        else:
            curr=self.head
            while(curr.next!=None):
                curr=curr.next
            curr.next=temp     
    def add_first(self,e):
        temp=node(e)
        if(self.head==None):
            self.head=temp
        else:
            temp.next=self.head
            self.head=temp       
    def add_elemenet_st(self,index,element):
        try:
            if(index==0):
                self.add_first(element)
            else:
                temp=node(element)
                count=0
                curr=self.head
                while(count<index-1):
                    curr=curr.next
                    count=count+1
                temp.next=curr.next
                curr.next=temp
        except AttributeError:
            raise IndexError('index'+str(index)+'does not exist')    
    def add_all(self,elements):
        for element in elements:
            self.add(element)                              
ll=Linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)
# ll.add_elemenet_st(2,100)
elements=[1,2,3,4,5,6]
ll.add_all(elements)
ll.printlinkedlist()


# remove first element
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def printlinkedlist(self):
        curr=self.head
        while(curr!=None):
            print(curr.data)
            curr=curr.next 
    def add(self,e):
        temp=node(e)      
        if(self.head==None):
            self.head=temp
        else:
            curr=self.head
            while(curr.next!=None):
                curr=curr.next
            curr.next=temp     
    def add_first(self,e):
        temp=node(e)
        if(self.head==None):
            self.head=temp
        else:
            temp.next=self.head
            self.head=temp       
    def add_elemenet_st(self,index,element):
        try:
            if(index==0):
                self.add_first(element)
            else:
                temp=node(element)
                count=0
                curr=self.head
                while(count<index-1):
                    curr=curr.next
                    count=count+1
                temp.next=curr.next
                curr.next=temp
        except AttributeError:
            raise IndexError('index'+str(index)+'does not exist')    
    def add_all(self,elements):
        for element in elements:
            self.add(element) 
    def remove_first(self):
        if(self.head==None):
            print("no element in linked list")
        elif self.head==None:
            self.head=None
        elif self.head!=None:
            curr=self.head
            self.head=self.head.next
            curr.next=None                             
ll=Linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)
# ll.add_elemenet_st(2,100)
# elements=[1,2,3,4,5,6]
# ll.add_all(elements)
ll.remove_first()
ll.remove_first()
ll.remove_first()
ll.printlinkedlist()


# REMOVE LAST ELEMENT
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def printlinkedlist(self):
        curr=self.head
        while(curr!=None):
            print(curr.data)
            curr=curr.next 
    def add(self,e):
        temp=node(e)      
        if(self.head==None):
            self.head=temp
        else:
            curr=self.head
            while(curr.next!=None):
                curr=curr.next
            curr.next=temp     
    def add_first(self,e):
        temp=node(e)
        if(self.head==None):
            self.head=temp
        else:
            temp.next=self.head
            self.head=temp       
    def add_elemenet_st(self,index,element):
        try:
            if(index==0):
                self.add_first(element)
            else:
                temp=node(element)
                count=0
                curr=self.head
                while(count<index-1):
                    curr=curr.next
                    count=count+1
                temp.next=curr.next
                curr.next=temp
        except AttributeError:
            raise IndexError('index'+str(index)+'does not exist')    
    def add_all(self,elements):
        for element in elements:
            self.add(element) 
    def remove_first(self):
        if(self.head==None):
            print("no element in linked list")
        elif self.head==None:
            self.head=None
        elif self.head!=None:
            curr=self.head
            self.head=self.head.next
            curr.next=None  
    def remove_last(self):
        if(self.head==None):
            print("no elements in linked list")
        elif self.head.next==None:
            self.head=None
        elif self.head.next!=None:
            curr=self.head
            while(curr.next.next!=None):
                curr=curr.next
            curr.next=None                                               
ll=Linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)
# ll.add_elemenet_st(2,100)
# elements=[1,2,3,4,5,6]
# ll.add_all(elements)
# ll.remove_first()
# ll.remove_first()
# ll.remove_first()
ll.remove_last()
ll.remove_last()
ll.remove_last()
ll.printlinkedlist()


# INDEXOF

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def printlinkedlist(self):
        curr=self.head
        while(curr!=None):
            print(curr.data)
            curr=curr.next 
    def add(self,e):
        temp=node(e)      
        if(self.head==None):
            self.head=temp
        else:
            curr=self.head
            while(curr.next!=None):
                curr=curr.next
            curr.next=temp     
    def add_first(self,e):
        temp=node(e)
        if(self.head==None):
            self.head=temp
        else:
            temp.next=self.head
            self.head=temp       
    def add_elemenet_st(self,index,element):
        try:
            if(index==0):
                self.add_first(element)
            else:
                temp=node(element)
                count=0
                curr=self.head
                while(count<index-1):
                    curr=curr.next
                    count=count+1
                temp.next=curr.next
                curr.next=temp
        except AttributeError:
            raise IndexError('index'+str(index)+'does not exist')    
    def add_all(self,elements):
        for element in elements:
            self.add(element) 
    def remove_first(self):
        if(self.head==None):
            print("no element in linked list")
        elif self.head==None:
            self.head=None
        elif self.head!=None:
            curr=self.head
            self.head=self.head.next
            curr.next=None  
    def remove_last(self):
        if(self.head==None):
            print("no elements in linked list")
        elif self.head.next==None:
            self.head=None
        elif self.head.next!=None:
            curr=self.head
            while(curr.next.next!=None):
                curr=curr.next
            curr.next=None  
    def index_of(self,element):
        curr=self.head
        count=0
        while(curr!=None):
            if(curr.data==element):
                return count
            curr=curr.next
            count=count+1
        return -1    

ll=Linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)
# ll.add_elemenet_st(2,100)
# elements=[1,2,3,4,5,6]
# ll.add_all(elements)
# ll.remove_first()
# ll.remove_first()
# ll.remove_first()
# ll.remove_last()
# ll.remove_last()
# ll.remove_last()
print(ll.index_of(30))
ll.printlinkedlist()

# last index of
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def printlinkedlist(self):
        curr=self.head
        while(curr!=None):
            print(curr.data)
            curr=curr.next 
    def add(self,e):
        temp=node(e)      
        if(self.head==None):
            self.head=temp
        else:
            curr=self.head
            while(curr.next!=None):
                curr=curr.next
            curr.next=temp     
    def add_first(self,e):
        temp=node(e)
        if(self.head==None):
            self.head=temp
        else:
            temp.next=self.head
            self.head=temp       
    def add_elemenet_st(self,index,element):
        try:
            if(index==0):
                self.add_first(element)
            else:
                temp=node(element)
                count=0
                curr=self.head
                while(count<index-1):
                    curr=curr.next
                    count=count+1
                temp.next=curr.next
                curr.next=temp
        except AttributeError:
            raise IndexError('index'+str(index)+'does not exist')    
    def add_all(self,elements):
        for element in elements:
            self.add(element) 
    def remove_first(self):
        if(self.head==None):
            print("no element in linked list")
        elif self.head==None:
            self.head=None
        elif self.head!=None:
            curr=self.head
            self.head=self.head.next
            curr.next=None  
    def remove_last(self):
        if(self.head==None):
            print("no elements in linked list")
        elif self.head.next==None:
            self.head=None
        elif self.head.next!=None:
            curr=self.head
            while(curr.next.next!=None):
                curr=curr.next
            curr.next=None  
    def index_of(self,element):
        curr=self.head
        count=0
        while(curr!=None):
            if(curr.data==element):
                return count
            curr=curr.next
            count=count+1
        return -1    
    def last_index_of(self,element):
        curr=self.head
        count=0
        index=-1
        while(curr!=None):
            if(curr.data==element):
                return count
            curr=curr.next
            count=count+1
        return index    

ll=Linkedlist()
ll.add(40)
ll.add(20)
ll.add(30)
ll.add(40)
# ll.add_elemenet_st(2,100)
# elements=[1,2,3,4,5,6]
# ll.add_all(elements)
# ll.remove_first()
# ll.remove_first()
# ll.remove_first()
# ll.remove_last()
# ll.remove_last()
# ll.remove_last()
print(ll.last_index_of(30))
ll.printlinkedlist()
