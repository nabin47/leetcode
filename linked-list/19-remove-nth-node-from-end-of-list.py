# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Iterative

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        size = 0
        while temp != None:
            temp = temp.next
            size += 1
        prev = None
        cur = head
        for i in range(size-n):
            prev = cur
            cur = cur.next
        if prev == None:
            return head.next
        prev.next = cur.next
        return head