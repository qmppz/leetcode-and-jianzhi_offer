'''
jianzhi-offer-合并两个排序的链表
https://www.nowcoder.com/practice/d8b6b4358f774294a89de2a6ac4d9337?tpId=13&tqId=11169&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        '''
        思路：phead1为最后返回的序列，现将phead2逐个插入phead1中，
        遍历phead2，对于每一个值找到在phead1中的位置，然后插入
        
        '''
        
        if not pHead1 or not pHead2: return pHead1 if not pHead2 else pHead2
        pre_n1=None
        resHead = pHead1
        if pHead1.val > pHead2.val:
            pHead1, pHead2 = pHead2, pHead1
        while pHead2:
            newNode = ListNode(pHead2.val)
            while newNode.val >= pHead1.val:
                pre_n1 = pHead1
                if pHead1.next:
                    pHead1 = pHead1.next
                else:
                    pHead1.next = pHead2
                    return resHead
            else:
                if pre_n1:
                    pre_n1.next=newNode
                newNode.next = pHead1
                pre_n1 = newNode
            pHead2 = pHead2.next
        return resHead
                
                
                
                