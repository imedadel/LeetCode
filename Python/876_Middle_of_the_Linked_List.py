# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # A = [head]
        # while A[-1].next:
        #     A.append(A[-1].next)
        # return A[len(A) // 2]
        
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
        return s
