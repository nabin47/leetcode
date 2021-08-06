# Time Complexity: O(n^2) solution. 
# Space Complexity: O(n^2) as a list of list is created.
# [Where n = numRows]
# Approach: Iterative / DP

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        pas_triangle = [[1], [1, 1]]
        i = 2
        while i < numRows:
            k = 0
            n = len(pas_triangle[i-1])
            temp = [1]
            while k + 1 < n:
                temp.append(pas_triangle[i-1][k] + pas_triangle[i-1][k+1])
                k += 1
            temp.append(1)
            pas_triangle.append(temp)
            i += 1
        return pas_triangle
