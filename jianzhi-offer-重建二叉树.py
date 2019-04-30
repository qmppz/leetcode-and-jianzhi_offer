'''
jianzhi-offer 重建二叉树
https://www.nowcoder.com/practice/8a19cbe657394eeaac2f6ea9b0f6fcf6?tpId=13&tqId=11157&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking

题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。


'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        '''
        方法一：
        <前先序  ^中序
        注意： string类型的话可用find方法去查找字符串位置，list没有find方法
        '''
        global pre_i #函数内部的全局变量，定义是需要声明，使用时也需要声明
        pre_i=0
        def buildBT(s,e):
            global pre_i ##函数内部的全局变量，定义是需要声明，使用时也需要声明
            if s>e or pre_i>=len(tin):return None
            mid_i = tin.index(pre[pre_i],s,e+1)
            midNode = TreeNode(tin[mid_i])
            pre_i=pre_i+1
            #left
            if mid_i>s:
                midNode.left = buildBT(
                    s=s, e=mid_i - 1 
                )                                    
            else:  midNode.left=None
            
            if mid_i<e:
                midNode.right = buildBT(
                s=mid_i+1, e=e
                )
            else: midNode.right=None
                
            return midNode
        
        return buildBT(0,len(tin))

            
            
        
        