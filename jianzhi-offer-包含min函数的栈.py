'''
jianzhi-offer-包含min函数的栈
https://www.nowcoder.com/practice/4c776177d2c04c2494f2555c9fcc1e49?tpId=13&tqId=11173&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

'''

# -*- coding:utf-8 -*-
class Solution:
    __stack=[]
    __min_idx=-1
    def push(self, node):
        # write code here
        self.__stack.append(node)
        if self.__min_idx>=0:
            if self.__stack[self.__min_idx] > node:
                self.__min_idx = len(self.__stack)-1
        else: self.__min_idx = 0
        
    def pop(self):
        # write code here
        if len(self.__stack)>0:
            returnVal = self.__stack.pop(-1)
            self.__min_idx = self.__stack.index(min(self.__stack)) if len(self.__stack)>0 else -1
            return returnVal
        return None
    
    def top(self):
        # write code here
        return self.__stack[-1] if len(self.__stack)>0 else None
    
    def min(self):
        # write code here
        return self.__stack[self.__min_idx] if len(self.__stack)>0 else None