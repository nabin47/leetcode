# Time complexity: O(n)
# Space complexity: O(1)
# Approach: Iterative

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        previous = head
        current = head.next
        while current:
            while current and current.val == previous.val:
                current = current.next
            previous.next = current
            previous = current
            if current:
                current = current.next
        return head
