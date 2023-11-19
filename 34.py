def insertNode(head, val):
    newNode = Node(val)
    if head == None:
        head = newNode
        return head
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = newNode
    return head




# utility function to check if the linked list is palindrome or not
def isPalindrome(head):
    arr = []
    while head != None:
        arr.append(head.val)
        head = head.next
    for i in range(len(arr)//2):
        if arr[i] != arr[len(arr)-i-1]:
            return False
    return True




if __name__ == "__main__":
    head = None
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 3)
    head = insertNode(head, 2)
    head = insertNode(head, 1)
    print(isPalindrome(head))
