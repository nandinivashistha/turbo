class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        temp = head
        for i in range(n // 2):
            temp = temp.next
        return temp
