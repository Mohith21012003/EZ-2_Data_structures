class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def get_length(circular_list):
    if not circular_list:
        return 0

    length = 1
    current = circular_list.next
    while current != circular_list:
        length += 1
        current = current.next

    return length

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1 
length = get_length(node1)
print("Length of the circular linked list:", length)
