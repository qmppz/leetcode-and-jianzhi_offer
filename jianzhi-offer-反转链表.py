'''
jianzhi-offer-反转链表
https://www.nowcoder.com/practice/75e878df47f24fdc9dc3e400ec6058ca?tpId=13&tqId=11168&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


题目描述
输入一个链表，反转链表后，输出新链表的表头。
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pren=None
        while pHead:
            nextn=pHead.next
            pHead.next=pren
            pren=pHead
            pHead=nextn
        return pren
        