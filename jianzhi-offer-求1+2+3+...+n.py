'''
jianzhi-offer-求1+2+3+...+n
https://www.nowcoder.com/practice/7a0da8fc483247ff8800059e12d7caf1?tpId=13&tqId=11200&rp=2&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tPage=3


题目描述
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''


# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        '''
        方法1：
        主要，python 等号赋值是没有返回值的
        
        要注意python中逻辑运算符的用法，a  and  b，a为False，返回a，a为True，就返回b
        '''
        res = n
        #n-1 and res=self.Sum_Solution(n-1) #是不成功的，res=赋值式子没有返回值，也就无法逻辑运算
        #要注意python中逻辑运算符的用法，a  and  b，a为False，返回a，a为True，就返回b
        bool_or_num =  n-1 and  self.Sum_Solution(n-1)# bool_or_num可能是bool型，也可能是数值型
        return res+bool_or_num