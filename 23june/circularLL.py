class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLL:
    def __init__(self):
        self.head=None
        self.tail=None
node_1=Node(10)
node_2=Node(20)
node_3=Node(30)
node_4=Node(40)
node_5=Node(50)

print(node_1)
print(node_1)

print(node_2)

print(node_3)

cl=CLL()

node_1.next=node_2
cl.head = node_1
cl.tail = node_2
cl.tail.next=cl.head
print(cl.tail.next)
print(cl.tail.next)

print(node_1.next)
print(node_1.next)

print(cl.tail.next)
print(cl.tail.next)

print(node_2.next)
print(node_2.next)

node_2.next=node_3
cl.head=node_2
cl.tail=node_3
cl.tail.next=cl.head

node_2.next=node_3
cl.head=node_2
cl.tail=node_3
cl.tail.next=cl.head

print(cl.tail.next)
print(cl.tail.next)

print(node_2.next)
print(node_2.next)

print(cl.tail.next)

print(node_3.next)
print(node_3.next)

node_3.next=node_4
cl.head=node_3
cl.tail=node_4
cl.tail.next=cl.head
node_4.next=node_5
cl.head=node_4
cl.tail=node_5
cl.tail.next=cl.head

print(cl.tail.next)
print(cl.tail.next)

print(node_3.next)
print(node_3.next)

print(node_4.next)
print(node_4.next)

node_4.next=node_5
cl.head=node_4
cl.tail=node_5
cl.tail.next=cl.head
print(cl.tail)
print(node_5.next)

print(node_4.next)
def insert_begining(self,data):
    new_node=Node(data)
    if self.head is None:
        self.head =  new_node
        self.tail=new_node
        self.tail.next=self.head
    else:
        new_node.next=self.head
        self.head=new_node
        self.tail.next=self.head
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLL:
    def __init__(self):
        self.head=None
        self.tail=None
node_1=Node(10)
node_2=Node(20)
node_3=Node(30)
node_4=Node(40)
node_5=Node(50)
node_6=Node(60)
print(node_1)
print(node_2)
print(node_3)
cl=CLL()
cl.head = node_1
node_1.next = node_2
cl.tail = node_2
cl.tail.next = cl.head
print(cl.tail.next)
print(node_1.next)
print(cl.tail.next)
print(node_2.next)
node_2.next= node_3
cl.tail=node_3
cl.tail.next=cl.head
print(node_3.next)
node_3.next=node_4
node_4.next=node_5
node_5.next=node_6
cl.tail=node_6
cl.tail.next=cl.head
print(node_6.next)'''
