'''
jianzhi-offer-把字符串转换成整数.py
https://www.nowcoder.com/practice/1277c681251b4372bdef344468e4f26e?tpId=13&tqId=11202&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

题目描述
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0
示例1
输入
复制
+2147483647
    1a33
输出
复制
2147483647
    0
'''


# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        '''
        思路一： ord(c) 转为ascII码  chr(num)转为字符
        '''
        if not s.strip(): return 0
        ascii_0 = ord('0')
        ascii_9 = ord('9')
        ten_x  = 1
        res_num = 0
        s = s.strip()
        if s[0]=='-' or s[0]=='+':
            ten_x = -1 if s[0]=='-' else 1
            s=s[1:]
        elif ord(s[0]) < ascii_0 or ord(s[0]) > ascii_9:
            return 0
        
        for e in s.strip()[::-1]:
            num = ord(e)
            if num >= ascii_0 and num <= ascii_9:
                res_num += (num-ascii_0)*ten_x
                ten_x *= 10
            else:
                res_num=0
                break
        return res_num
        