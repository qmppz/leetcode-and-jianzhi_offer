'''
jianzhi-offer-左旋转字符串
https://www.nowcoder.com/practice/12d959b108cb42b1ab72cef4d36af5ec?tpId=13&tqId=11196&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

题目描述
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
'''
# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        '''
        思路一：一行py搞定
        '''
        return s[n:]+s[:n]
        '''
        思路二：
        链接：https://www.nowcoder.com/questionTerminal/12d959b108cb42b1ab72cef4d36af5ec
        来源：牛客网

        假设字符串abcdef，n=3，设X=abc，Y=def，
        所以字符串可以表示成XY，如题干，问如何求得YX。
        假设X的翻转为XT，XT=cba，同理YT=fed，那么YX=(XTYT)T，三次翻转后可得结果。
        '''
        def T(lt,s,e):
            return lt[e:s-1:-1]
        x, y = s[:n], s[n:]
        x = T(x,0,len(x)-1)
        y = T(y,0,len(y)-1)
        result_ROL = T(x+y,0,len(x+y)-1)
        
        return result_ROL