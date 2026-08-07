class Solution(object):

    def binary_search_left(self, nums, target):
        low = 0
        high = len(nums) - 1
        first = -1

        while low <= high:
            mid = (low + high) // 2

            if target == nums[mid]:
                first = mid
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return first

    def binary_search_right(self, nums, target):
        low = 0
        high = len(nums) - 1
        last = -1

        while low <= high:
            mid = (low + high) // 2

            if target == nums[mid]:
                last = mid 
                low = mid + 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return last

    def searchRange(self, nums, target):
        first = self.binary_search_left(nums, target)

        if first == -1:
            return [-1, -1]

        last = self.binary_search_right(nums, target)

        return [first, last]