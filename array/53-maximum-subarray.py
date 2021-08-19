# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Kadane's Algorithm

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        i = 1
        n = len(nums)
        while i < n:
            if nums[i] < (nums[i]+nums[i-1]):
                nums[i] = nums[i-1] + nums[i]
            if max_sum < nums[i]:
                max_sum = nums[i]
            i += 1
        return max_sum
