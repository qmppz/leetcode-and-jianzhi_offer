'''
jianzhi-offer-从上往下打印二叉树
https://www.nowcoder.com/practice/7fe2212963db4790b57431d9ed259701?tpId=13&tqId=11175&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        '''
        层先法，队列实现
        '''
        if not root: return []#return None 会报错#[object of type 'NoneType' has no len()
        printList=[]
        queue=[root]
        i=0
        while i<len(queue):
            ele=queue[i]
            printList.append(ele.val)
            i+=1
            if ele.left: queue.append(ele.left)
            if ele.right: queue.append(ele.right)
        return printList