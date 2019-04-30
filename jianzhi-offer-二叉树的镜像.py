'''
jianzhi-offer-二叉树的镜像
https://www.nowcoder.com/practice/564f4c26aa584921bc75623e48ca3011?tpId=13&tqId=11171&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

题目描述
操作给定的二叉树，将其变换为源二叉树的镜像。
二叉树的镜像定义：源二叉树 
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9   11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7   5

'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        '''
        递归的交换两个子树，注意子树为空的情况即可
        '''
        def mirrorBT(root):
            if not root.left and not root.right:
                return
            if not root.left:
                root.left = root.right 
                root.right = None
                mirrorBT(root.left)
            elif not root.right:
                root.right = root.left
                root.left = None
                mirrorBT(root.right)
            else:
                root.left, root.right = root.right, root.left
                mirrorBT(root.left)
                mirrorBT(root.right)
            return  
        if not root : return None
        mirrorBT(root)
        return root
            