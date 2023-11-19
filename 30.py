class Node:
    def __init__(self, num: int):
        self.num = num
        self.next = None




# function to insert node at the end of the list
def insertNode(head: Node, val: int) -> Node:
    newNode = Node(val)
    if head == None:
        head = newNode
        return head
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = newNode
    return head
