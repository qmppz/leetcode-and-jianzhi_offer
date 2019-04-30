'''
jianzhi-offer-链表中倒数第k个结点
https://www.nowcoder.com/practice/529d3ae5a407492994ad2a246518148a?tpId=13&tqId=11167&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

题目描述
输入一个链表，输出该链表中倒数第k个结点。

参考解法：
链接：https://www.nowcoder.com/questionTerminal/529d3ae5a407492994ad2a246518148a
来源：牛客网

最佳代码：Java代码，通过校验。代码思路如下：两个指针，先让第一个指针和第二个指针都指向头结点，然后再让第一个指正走(k-1)步，到达第k个节点。然后两个指针同时往后移动，当第一个结点到达末尾的时候，第二个结点所在位置就是倒数第k个节点了。。
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        '''
        节省空间的解法
        '''
        left=right=head
        for i in range(k):
            if not right: return None
            right=right.next
        while right:
            right=right.next
            left=left.next
        return left
        