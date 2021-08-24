# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Iterative

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = temp = None
        while l1 != None or l2 != None:
            sum = 0
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = 0
            if sum > 9:
                carry = 1
                sum = sum % 10
            new_node = ListNode(sum)
            if head == None:
                head = new_node
                temp = new_node
                continue
            temp.next = new_node
            temp = temp.next
        if carry == 1:
            temp.next = ListNode(1)
        return head
