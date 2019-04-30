
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        jinwei =  0
        l3 = l3Head = ListNode(-1)
        while l1 or l2:
            if not l1: l1 = ListNode(0)
            elif not l2: l2 = ListNode(0)
            r = l1.val +l2.val + jinwei
            if r > 9: r, jinwei = r-10, 1
            else: jinwei = 0
            l3Head.next = ListNode(r)
            l3Head = l3Head.next
            l1, l2 = l1.next, l2.next
        if jinwei == 1: l3Head.next = ListNode(jinwei)
        return l3.next

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def main():
    mycls = Solution()
    res = mycls.addTwoNumbers(l1,l2)

    print(res)

if __name__ == '__main__':
    main()
