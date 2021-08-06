# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Iterate through the array to check if the
#           element is greater than 9 or not

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # O(n) solution. Approach: Iterate through the array to check if the
        # element is greater than 9 or not.
        
        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] += 1
                break
        if i == -1:
            # new_ar = [1]
            # for digit in digits:
            #     new_ar.append(digit)
            # return new_ar
            digits.insert(0, 1)
        return digits
