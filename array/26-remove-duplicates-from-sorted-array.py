# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Two pointer

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #O(n^2) solution. TLE

        #########################################

        # n = len(nums)
        # i = j = 0
        # while i+1 < n:
        #     flag = 0
        #     if nums[i] == nums[i+1]:
        #         j = i+1
        #         while j < n:
        #             flag = 1
        #             nums[j-1] = nums[j]
        #             j += 1
        #     if flag == 0:
        #         i += 1
        #     else:
        #         n -= 1
        # return n
        
        #O(n) solution

        ##########################################
        
        i = 0
        j = 1
        n = len(nums)
        while j < n:
            while j < n and nums[i] == nums[j]:
                j += 1
            if j < n:
                i += 1
                nums[i] = nums[j]
                j += 1
        return i + 1
        