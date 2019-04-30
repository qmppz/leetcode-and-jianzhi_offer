'''
jianzhi-offer-调整数组顺序使奇数位于偶数前面

https://www.nowcoder.com/practice/beb5aa231adc45b2a5dcc5b62c93f593?tpId=13&tqId=11166&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''


# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        #没有意义的题
        return sorted(array,key=lambda c:1-c%2,reverse=False)    
        