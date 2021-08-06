# Time Complexity: O(m+n) 
# Space Complexity: O(1)
# Approach: Iterate the nums array from rear end.
# Trick: Keep 3 pointers

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if i < 0 or nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
            else:
                while i >= 0 and nums1[i] > nums2[j]:
                    nums1[k] = nums1[i]
                    i -= 1
                    k -= 1
                # nums1[k] = nums2[j]
                # j -= 1
            
        
