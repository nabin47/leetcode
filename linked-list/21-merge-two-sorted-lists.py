# Time Complexity: O(n+m)
# Space Complexity: O(m)
# Approach: Iterative

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            head = prev = None
            if l1.val <= l2.val:
                head = l1
            else:
                head = l2
            while l2 != None:
                while l1 != None and l1.val <= l2.val:
                    prev = l1
                    l1 = l1.next
                if l1 == None:
                    if prev == None:
                        l1 = l2
                        l1 = l1.next
                    else:
                        prev.next = l2
                        prev = prev.next
                    l2 = l2.next
                    continue
                temp = l2
                l2 = l2.next
                if prev != None:
                    prev.next = temp
                temp.next = l1
                prev = temp
        return head
