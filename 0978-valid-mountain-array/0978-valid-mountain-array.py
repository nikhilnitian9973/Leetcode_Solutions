class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        i = 0

        while arr[i] < arr[i+1]:
            i += 1

            if i == len(arr)-1:
                return False
        if i == 0:
            return False
        while arr[i] > arr[i+1]:
            i +=1
            if i == len(arr)-1:
                return True
        return False