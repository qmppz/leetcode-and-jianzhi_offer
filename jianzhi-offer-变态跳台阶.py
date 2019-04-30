'''
jianzhi-offer 变态跳台阶
https://www.nowcoder.com/practice/22243d016f6b47f2a6928b4313c85387?tpId=13&tqId=11162&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

'''

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        '''
        还是斐波那契数列变种
        跳上n级台阶为第一步，现在考虑倒数第二步， 
        第n级台阶可以由 n-1到 1 的台阶直接跳过来
        动态转移方程： f(N) =  就等于 2**(number)
        '''

        return 2**(number-1)