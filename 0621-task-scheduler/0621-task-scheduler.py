
class Solution:
    def leastInterval(self, tasks, n):
        count = {}
        for task in tasks:
            count[task] = count.get(task, 0) + 1
        maxCount = max(count.values())
        maxFreq = 0
        for item in count.values():
            if item == maxCount:
                maxFreq += 1
        
        return max(len(tasks), (maxCount-1)*(n+1)+maxFreq)