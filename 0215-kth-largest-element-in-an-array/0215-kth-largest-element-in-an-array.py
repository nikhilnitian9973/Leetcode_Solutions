class Solution(object):
    def heap_up(self,ind):
        if ind <= 0:
            return
        parent_node = (ind-1)//2
        if self.stack[parent_node] < self.stack[ind]:
            self.stack[parent_node],self.stack[ind]= self.stack[ind],self.stack[parent_node]
            self.heap_up(parent_node)
    def heap_down(self,ind):
        n = len(self.stack)
        left = 2*ind +1
        right = 2*ind+2
        large_ele_ind = ind
        if left < n and self.stack[large_ele_ind] < self.stack[left]:
            large_ele_ind = left
        if right < n and self.stack[large_ele_ind] < self.stack[right]:
            large_ele_ind = right
        if large_ele_ind != ind:
            self.stack[ind],self.stack[large_ele_ind] = self.stack[large_ele_ind],self.stack[ind]
            self.heap_down(large_ele_ind)

    def max_heap(self,nums):
        
        for i in range(len(nums)):
            self.push(nums[i])
        return self.stack
    def push(self,val):
        self.stack.append(val)
        if len(self.stack) >1:
            self.heap_up(len(self.stack)-1)
    def pop_top(self):
        
        self.stack[0],self.stack[-1] = self.stack[-1],self.stack[0]
        top = self.stack.pop()
        self.heap_down(0)
        

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.stack = []
        a = self.max_heap(nums)
        n = len(self.stack)
        for i in range(k-1):
            
            self.pop_top()
            
        return self.stack[0]