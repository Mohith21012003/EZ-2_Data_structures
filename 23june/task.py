class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def detect_loop(head):
    if head is None:
        return False

    slow_ptr = head
    fast_ptr = head.next

    while fast_ptr is not None and fast_ptr.next is not None:
        if slow_ptr == fast_ptr:
            return True

        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return False

head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = head  # Creating the loop

has_loop = detect_loop(head)
print("Loop detected:", has_loop)
