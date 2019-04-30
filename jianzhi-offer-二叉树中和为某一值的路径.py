'''
jianzhi-offer-二叉树中和为某一值的路径.py
https://www.nowcoder.com/practice/b736e784e3e34731af99065031301bca?tpId=13&tqId=11177&tPage=2&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

题目描述
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        '''
        思路一： 递归思想，构造函数 get_path(tree, expectNumber):->None 无返回值，使用全局变量保存结果
        递归的计算符合的路径，递归退出条件是 
        
        '''
        global res_path
        res_path = []
        # list 深拷贝
        import copy
        def get_path(tree, expectNumber, a_path):
            global res_path
            if not tree : return 
            a_path.append(tree.val)
            # expectNumber 递减为0，且这个节点是叶子节点
            if expectNumber - tree.val == 0 and not tree.left and not tree.right:
                res_path.append(a_path)
                return 
            
            get_path(tree.left, expectNumber - tree.val, copy.deepcopy(a_path))
            get_path(tree.right, expectNumber - tree.val, copy.deepcopy(a_path))
            
        get_path(root, expectNumber, [])
        return res_path
            
            
            
            
            
            
            
            
        
        