# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rslt = rsltTmp = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                rsltTmp.next = ListNode(l1.val)
                rsltTmp = rsltTmp.next
                l1 = l1.next
            else:
                rsltTmp.next = ListNode(l2.val)
                rsltTmp = rsltTmp.next
                l2 = l2.next
        if l1:
            rsltTmp.next = l1
        elif l2:
            rsltTmp.next = l2
        return rslt.next


        

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def main():
    mycls = Solution()
    res = mycls.mergeTwoLists(l1,l2)

    print(res)

if __name__ == '__main__':
    main()
