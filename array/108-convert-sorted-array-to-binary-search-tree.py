# Time complexity: O(n) solution. As we go through all of n elements once.
# Space complexity: O(logn). The stack size of recursion call
# Approach: Recursion

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(nums, 0, len(nums))
    
    def helper(self, nums, start, end):
        if start >= end:
            return None
        root_index = (start + end) // 2
        root = TreeNode(nums[root_index])
        root.left = self.helper(nums, start, root_index)
        root.right = self.helper(nums, root_index+1, end)
        return root
