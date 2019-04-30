'''
jianzhi-offer-链表中环的入口结点.py
https://www.nowcoder.com/practice/253d2c59ec3e4bc68da16833f79a38e4?tpId=13&tqId=11208&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

题目描述
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        '''
        方法一：
        T=O(N)
        空间复杂度 O(N)
        '''
        idSet=set()
        while pHead:
            if id(pHead) in idSet:
                return pHead
            idSet.add(id(pHead))
            pHead = pHead.next
            
        return None
        '''
        方法二：
        T=O(N)
        空间复杂度 O(1)
链接：https://www.nowcoder.com/questionTerminal/253d2c59ec3e4bc68da16833f79a38e4
来源：牛客网

假设x为环前面的路程（黑色路程），a为环入口到相遇点的路程（蓝色路程，假设顺时针走）， c为环的长度（蓝色+橙色路程）
当快慢指针相遇的时候：

此时慢指针走的路程为Sslow = x + m * c + a
快指针走的路程为Sfast = x + n * c + a
2 Sslow = Sfast
2 * ( x + m*c + a ) = (x + n *c + a)
从而可以推导出：
x = (n - 2 * m )*c - a
= (n - 2 *m -1 )*c + c - a
即环前面的路程 = 数个环的长度（为可能为0） + c - a
(前面的路程x 对 环的长度c取余数等于 c-a： x%c=c-a ;a为环入口到相遇点的路程)
什么是c - a？这是相遇点后，环后面部分的路程。（橙色路程）
所以，我们可以让一个指针从起点A开始走，让一个指针从相遇点B开始继续往后走，
2个指针速度一样，那么，当从原点的指针走到环入口点的时候（此时刚好走了x）
从相遇点开始走的那个指针也一定刚好到达环入口点。
所以2者会相遇，且恰好相遇在环的入口点。

最后，判断是否有环，且找环的算法复杂度为：

时间复杂度：O(n)

空间复杂度：O(1)
        '''
        p_slow = p_fast = pHead
        while p_fast and p_fast.next:
            p_slow = p_slow.next
            p_fast = p_fast.next.next
            if id(p_slow) == id(p_fast):
                #快慢指针 相遇
                #快指针回到开始位置，以步长为1的节奏从头开始遍历，直到再次相遇，相遇点即为环的开始节点
                p_fast = pHead
                while id(p_fast) != id(p_slow):
                    p_fast = p_fast.next
                    p_slow = p_slow.next
                return p_fast
        return None
        
            
            
            
        
        
        