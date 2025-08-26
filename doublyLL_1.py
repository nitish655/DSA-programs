# Python program to rotate a doubly-linked 
# list counter-clockwise by p positions
class Node:
    def __init__(self, x):
        self.data = x
        self.prev = None
        self.next = None
        
# Function to rotate the doubly-linked list
def rotateDLL(head, p):
    tail = head

    # Find the last node
    while tail.next:
        tail = tail.next

    # Make the list circular
    tail.next = head
    head.prev = tail

    # Move head and tail by the given position
    for i in range(p):
        head = head.next
        tail = tail.next

    # Break the circular connection
    tail.next = None
    head.prev = None

    return head

def printList(head):
    curr = head
    while curr:
        print(curr.data, end="")
        if curr.next:
            print(" ", end="")
        curr = curr.next
    print()

if __name__ == "__main__":
  
    head = Node(2)
    head.next = Node(6)
    head.next.prev = head
    head.next.next = Node(5)
    head.next.next.prev = head.next
    head.next.next.next = Node(4)
    head.next.next.next.prev = head.next.next

    p = 3
    head = rotateDLL(head, p)
    printList(head)