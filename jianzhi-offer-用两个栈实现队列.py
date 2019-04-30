'''
jianzhi-offer 用两个栈实现队列

https://www.nowcoder.com/practice/54275ddae22f475981afa2244dd448c6?tpId=13&tqId=11158&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

参考题解：
https://www.cnblogs.com/hwf-73/p/7705100.html
'''

# -*- coding:utf-8 -*-
class Solution:
    stack_pop=[]
    stack_push=[]
    def push(self, node):
        # write code here
        '''
        使用 list 模拟 stack 
        stack_push 作为添加元素的栈
        '''
        self.stack_push.append(node)
        
    def pop(self):
        # return xx
        '''
        stack_pop 作为模拟出队列的栈
        '''
        if len(self.stack_pop)>0:
            return self.stack_pop.pop(-1)
        else:
            #pop栈元素个数为0,
            if len(self.stack_push)>0:
                #push栈里面还有元素，将其放入 pop中
                while len(self.stack_push)>0:
                    self.stack_pop.append(self.stack_push.pop(-1))
                return self.stack_pop.pop(-1)
            else:
                #没有元素，删除失败
                return None
        
        
        