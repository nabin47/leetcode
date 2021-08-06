# Time Complexity: O(n) [Using two pointer]
# Space Complexity:O(1) 
# Approach: Two pointer/ Sorting

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #O(nlogn) solution. Approach: Sorting
        
        #########################################
        
        # i = 0
        # j = 0
        # flag = 0
        # n = len(nums)
        # sorted(nums)
        # while j < n:
        #     while j < n and nums[j] == val:
        #         j += 1
        #         flag = 1
        #     if j < n and flag == 1:
        #         nums[i] = nums[j]
        #         i += 1
        #         j += 1
        #     elif flag == 0:
        #         i += 1
        #         j += 1
        # if flag == 0:
        #     return i + 1
        # else:
        #     return i
        
        #O(n) solution. Approach: Two pointer
        
        ###########################################
        i = 0
        j = 0
        n = len(nums)
        while j < n:
            while j < n and nums[j] == val:
                j += 1
            if j < n:
                nums[i] = nums[j]
                i += 1
                j += 1
        return i
        
            
        
