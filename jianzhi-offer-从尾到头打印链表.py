'''
jianzhi-offer 从尾到头打印链表
https://www.nowcoder.com/practice/d0267f7f55b3412ba93bd35cfa8e8035?tpId=13&tqId=11156&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

题目描述
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:return []
        res=[]
        while listNode:
            res.append(listNode.val)
            listNode=listNode.next
        
        return list(reversed(res)) #res[::-1]#res[-1::-1]
    #res.reverse() 返回 None ,这是直接内部改变 res，不返回
    #reversed(res) str int都错误，都返回<list_reverseiterator object at 0x000002F566327940>
    #一个迭代器，reversed(seq)是将序列（seq）反转，返回一个迭代器。
    #正确用法：
    #list(reversed(seq)) #就可以了
    #https://www.cnblogs.com/xsmile/p/8074458.html
    