'''
jianzhi-offer-二进制中1的个数
https://www.nowcoder.com/practice/8ee967e43c2c4ec193b040ea7fbb10b8?tpId=13&tqId=11164&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        '''
        方法一
        利用函数 bin求二进制,会产生前缀0b,
        对负数特别处理
>>> bin(1)
'0b1'
>>> bin(-1)
'-0b1'
        '''
        #eooro# return bin(n).count('1') if n>=0 else bin(~n+1).count('1')
        '''
        参考解法：n = n & (n-1);   每次 与 操作都把最右边的一个1去掉，但是对于负数 -1 会陷入死循环
        链接：https://www.nowcoder.com/questionTerminal/8ee967e43c2c4ec193b040ea7fbb10b8
来源：牛客网

如果一个整数不为0，那么这个整数至少有一位是1。如果我们把这个整数减1，那么原来处在整数最右边的1就会变为0，原来在1后面的所有的0都会变成1(如果最右边的1后面还有0的话)。其余所有位将不会受到影响。
        '''
        #对于负数，先将位数限制为32位，并将符号位转换成数值位
        #n = n & 0xffffffff， 这个代码在python中是将最高位的符号位变成表示数值的1。比如复数，最高位1表示负号，但是这么一与，最高位的1不在表示负号，而是表示数值
        if n < 0:
            #这样 n就转换成了正数，进行移位操作就不会死循环了
            #负数进行位运算时，默认使用 其补码运算，所以下面的式子得到的结果是
            #将 n 的补码的符号位转换成数值位的形式，这样就保留了所有的1，且n作为一个正数，移位不会死循环
            n = n & 0xffffffff
        
        cnt=0
        while n!=0:
            cnt+=1
            n = n & (n-1)
        return cnt 