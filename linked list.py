class node:

    def __init__(self,data):
        self.data=data
        self.next=None
 #*************************************
class linked_list:
    def __init__(self):
        self.head=None
        print()
 #*************************************
        """
    def push(self, new_data):
        new_node =node(new_data)      #insert in beginning 
        new_node.next =self.head
        self.head = new_node
     """
 #*************************************
    def inserAtEnd(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node         #insert at end
            return
        last=self.head
        while (last.next):
            last=last.next
            #last.next=new_node
 #*************************************	
    """
    def append(self,new_data):
        new_node =node(new_data)
        if self.head==None:
            self.head=new_node
            return
            last=self.head
            while (last.next):
                last=last.next
                last.next=new_node
        """
 #*************************************
    def printlist(self):
        temp=self.head
        while (temp):
            print(temp.data)
            temp=temp.next
 #*************************************
s2=node(9)
s2=linked_list()
"""
s2.push(8)
s2.append(7)
s2.push(4)
s2.push(5)
s2.printlist()
"""
s2.inserAtEnd(8)
s2.inserAtEnd(4)
s2.inserAtEnd(5)
s2.printlist()














