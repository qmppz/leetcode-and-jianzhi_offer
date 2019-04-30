'''
jianzhi-offer-对称的二叉树.py

https://www.nowcoder.com/practice/ff05d44dfdb04e1d83bdbdab320efbcb?tpId=13&tqId=11211&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
题目描述
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        '''
        二叉树镜像的定义：对每一个节点都做【交换左右孩子】的操作得到的即为二叉树镜像
        对称二叉树定义：以根节点为中轴线对折，能重合
        '''
        '''
        思路一：递归判断左右孩子是否对称
        def pf(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val == right.val:
                return pf(left.right, right.left) and \
                       pf(left.left, right.right)
            else:
                return False
        return pf(pRoot.left, pRoot.right) if pRoot else True
                '''
        '''
        思路二：非递归方法
        
        '''
        
        
        