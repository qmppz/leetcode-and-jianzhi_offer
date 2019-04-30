'''
jianzhi-offer 斐波那契数列

https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?tpId=13&tqId=11160&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

'''
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        '''
        递归肯定不行
        
        f = [0,1]
        for i in range(2,n+1):
            f.append(f[i-1]+f[i-2])
        return f[n]
        '''
        '''
        方法二：节省空间法
        只用两个变量
        '''
        if n<=1:return n
        now, last=1,0
        for i in range(2,n+1):
            now += last
            last = now - last
        return now 
        