'''
jianzhi-offer-矩形覆盖
https://www.nowcoder.com/practice/72a5a919508a4251859fb2cfb987a0e6?tpId=13&tqId=11163&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        '''
        硬找规律；f1 = 1, f2=2,fn=f(n-1)+f(n-2)
        '''
        f=[0,1,2,3]
        for i in range(4,number+1):
            f.append(f[i-1]+f[i-2])
        return f[number]
        