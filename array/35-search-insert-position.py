# Time Complexity: O(logn)
# Space Complexity: O(1)
# Approach: Binary search

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        prev_ind = 0
        
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
            prev_ind = mid
        if nums[prev_ind] > target:
            return prev_ind
        else:
            return prev_ind + 1
        
