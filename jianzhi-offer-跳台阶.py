'''
jianzhi-offer 跳台阶
https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4?tpId=13&tqId=11161&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
跳台阶
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        '''
        斐波拉契数列的变种，初始序列不同
        动态规划问题：
        转移方程为： f(N) = f(N-1) + f(N-2)
        '''
        if number<=3:return number
        res=[0,1,2]
        for i in range(3,number+1):
            res.append( res[i-1] + res[i-2])
        return res[number]