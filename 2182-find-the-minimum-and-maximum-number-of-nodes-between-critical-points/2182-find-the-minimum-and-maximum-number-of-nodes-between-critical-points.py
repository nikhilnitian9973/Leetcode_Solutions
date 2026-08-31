# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        prev= head
        curr = head.next
        idx = 1
        first_Critical = -1
        last_Critical = -1
        minDist = float('inf')


        while curr.next:
            next_node = curr.next

            isMax = curr.val > prev.val and curr.val > next_node.val
            isMin = curr.val < prev.val and curr.val < next_node.val

            if isMax or isMin:

                if last_Critical == -1:
                    first_Critical = idx
                else:
                    minDist = min(minDist,idx-last_Critical)

                last_Critical = idx
            prev = curr
            curr = next_node
            idx  +=1
        
        if first_Critical == -1 or first_Critical == last_Critical:
            return [-1,-1]
        
        return [minDist,last_Critical - first_Critical]