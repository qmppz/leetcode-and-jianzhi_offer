'''
jianzhi-offer-树的子结构
https://www.nowcoder.com/practice/6e196c44c7004d15b1610b9afca8bd88?tpId=13&tqId=11170&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        '''
        方法一:
        参考解法：
        链接：https://www.nowcoder.com/questionTerminal/6e196c44c7004d15b1610b9afca8bd88
        来源：牛客网

        /*思路：参考剑指offer
        1、首先设置标志位result = false，因为一旦匹配成功result就设为true，
        剩下的代码不会执行，如果匹配不成功，默认返回false
        2、递归思想，如果根节点相同则递归调用DoesTree1HaveTree2（），
        如果根节点不相同，则判断tree1的左子树和tree2是否相同，
        再判断右子树和tree2是否相同
        3、注意null的条件，HasSubTree中，如果两棵树都不为空才进行判断，
        DoesTree1HasTree2中，如果Tree2为空，则说明第二棵树遍历完了，即匹配成功，
        tree1为空有两种情况（1）如果tree1为空&&tree2不为空说明不匹配，
        （2）如果tree1为空，tree2为空，说明匹配。

        */
        '''
        if not pRoot1 or not pRoot2: return False
        
        def DoesTree1HasTree2(proot1, proot2):
            if not proot2:
                return True
            elif not proot1:
                return False
            elif(proot1.val == proot2.val):
                return DoesTree1HasTree2(proot1.left,proot2.left) \
                            and DoesTree1HasTree2(proot1.right,proot2.right)
            return False
        #levelOrder proot1
        q_idx=0
        queue = [pRoot1]
        while q_idx<len(queue):
            elem = queue[q_idx]
            q_idx+=1
            result = DoesTree1HasTree2(elem,pRoot2)
            if result:return True
            
            if elem.left: queue.append(elem.left)
            if elem.right: queue.append(elem.right)
        return False


                
                
                
        
        
        
        