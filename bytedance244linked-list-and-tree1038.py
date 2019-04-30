# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverseRecursive(l:ListNode):
            if not l.next:return [l,l]
            else: 
                l_tmp, head = reverseRecursive(l.next)    
                l_tmp.next = l
                l.next = None
                return [l,head]
        #return reverseRecursive(head)[1] if head else None
        newHead = None
        while head:
            nextNode = head.next
            head.next = newHead
            newHead = head
            head = nextNode
        return newHead



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def main():
    l = [1,2,3,4,5]
    head = headTmp = ListNode(-1)
    for x in l:
        headTmp.next = ListNode(x)
        headTmp = headTmp.next
    mycls = Solution()
    res = mycls.reverseList(head=head.next)

    while res:
           print(res.val)
           res = res.next

if __name__ == '__main__':
    main()
 
