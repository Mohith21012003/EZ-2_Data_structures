class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("empty list")
        else:
            temp=self.head
        while temp:
            print(temp.data,"-->",end=" ")
            temp=temp.next
    def insert_begining(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_end(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.next=None
    def insert_position(self,pos,data):
        new_node=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
    def delete_begining(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def delete_end(self):
        prev = self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
    def delete_position(self,position):
        prev=self.head
        temp=self.head.next
        for i in range(1,position-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
node_1=Node("Mohith")
sl=SLL()
sl.head=node_1
node_2=Node("Siddartha")
node_3=Node("virat")
node_4=Node("Dhoni")
node_1.next=node_2
print(node_1.next)
node_3.next=node_4
print(node_3.next)
node_2.next=node_3
print(node_2.next)
sl.insert_begining("NEHA")
print(sl.head.data)
sl.insert_end("Mohith")
sl.insert_position(3,"jhon")
sl.delete_begining()
sl.delete_end()
sl.delete_position()
sl.display()