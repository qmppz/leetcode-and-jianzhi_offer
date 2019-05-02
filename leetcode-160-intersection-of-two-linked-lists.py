'''
leetcode-160-intersection-of-two-linked-lists.py
相交链表
https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
#

编写一个程序，找到两个单链表相交的起始节点。
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        
        
        """
        '''
        
        思路二：T=O(M+N) 比取长度差值同步遍历的做法更快;
                S=O(1) 空间还是O(1)
        参考题解：https://www.jianshu.com/p/9bb328b68021
        由题目可知：
            headA = 【a1->a2->a3->a4->a5】 + 【common】; 
            headB = 【b1->b2】 + 【common】;
        其中 common为公共链表部分，a，b分别为各自不同的部分
        则可构造新的链表
            NewHeadA链表：headA + headB = a + common + b + common 
                NewHeadA =
                【a1->a2->a3->a4->a5】+【common】+【b1->b2】+【common】
              
            NewHeadB链表：headB + headA = b + common + a + common
                NewHeadB=
                【b1->b2】+【common】+【a1->a2->a3->a4->a5】+【common】
        
        可见长度相同；
        那么对两个新链表从头开始，同步遍历，就一定能找到第一个相同的节点，也就是【common】的第一个
        
        
        '''
        #headA = a + common;
        #newheadA = headA + headB = a + common + b + common 
        
        nodeA, nodeB = headA, headB
        #只能拼接一次
        flag_A_concat_B, flag_B_concat_A = False, False
        while id(nodeA) != id(nodeB):
            #newheadA = headA + headB     = a + common + b + common 
            #nodeA 为空时，接上链表headB，继续循环
            if not nodeA:
                if flag_A_concat_B == True:
                    #走到头，且已经拼接过了，那么不存在交叉节点
                    break
                nodeA = headB 
                #只能拼接一次
                flag_A_concat_B = True
            else:
                nodeA = nodeA.next
            #nodeB 为空时，接上链表headA，继续循环
            if not nodeB:
                if flag_B_concat_A == True:
                    #走到头，且已经拼接过了，那么不存在交叉节点
                    break
                nodeB = headA
                #只能拼接一次
                flag_B_concat_A = True
            else:
                nodeB = nodeB.next
        
        return None if not nodeA or not nodeB else nodeA
        
        #--------------------------------------------
        '''
        思路一：T=O(M+N+min(M,N))； S=O(1) 
        先分别遍历获取两个列表的长度，得到长度的差值，以这个差值初始化 A 和 B 的开始节点，然后同时前进，直到相遇，即为相交节点
        '''
        lenA, lenB = 0, 0
        _nodeA, _nodeB = headA, headB
        while _nodeA:
            lenA += 1
            _nodeA = _nodeA.next
        while _nodeB:
            lenB += 1
            _nodeB = _nodeB.next
        chazhi = abs(lenA-lenB)
        #默认 headA 比较短
        headA, headB = [headB, headA] if lenA>lenB else [headA, headB]
        #A短，B长，B先前进chazhi个节点
        for i in range(chazhi):
            headB = headB.next
        #同步向前比较
        while headA and headB:
            #if headA.val == headB.val:
            #比较节点是否相同，而不是val值
            if id(headA) == id(headB):
                return headA
            headA = headA.next
            headB = headB.next
            
        return None