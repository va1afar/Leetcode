# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list = []
        sum = 0

        while head:
            if head.val == 0:
                if sum:
                    list.append(sum)
                sum = 0
            else:
                sum += head.val
            head = head.next

        a = ListNode(0)
        tmp = a

        for i in list:
            tmp.next = ListNode(i)
            tmp = tmp.next
            
        return a.next
        