# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def integer_to_sll(self,num):
        if num == 0:
            return ListNode(0)
        
        
        head = ListNode()
        curr = head
        while num >0:
            a = num %10
            node =  ListNode(a)
            curr.next = node
            curr = curr.next
            
            num //=10
        return head.next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        a = 0
        place= 1
        curr = l1
        while curr:
            a +=curr.val*place
            place *= 10
            curr = curr.next
            
            
        b = 0
        place = 1
        curr = l2
        while curr:
            b  += curr.val * place
            place *= 10
            curr = curr.next
        c = a+b
        return self.integer_to_sll(c)
