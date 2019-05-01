'''
程序员面试金典_ 编程题-另类加法.py
https://www.nowcoder.com/practice/e7e0d226f1e84ba7ab8b28efc6e1aebc?tpId=8&tqId=11065&rp=1&ru=%2Factivity%2Foj&qru=%2Fta%2Fcracking-the-coding-interview%2Fquestion-ranking&tPage=4

题目描述
请编写一个函数，将两个数字相加。不得使用+或其他算数运算符。

给定两个int A和B。请返回A＋B的值

测试样例：
1,2
返回：3

'''

# -*- coding:utf-8 -*-

class UnusualAdd:
    def addAB(self, A, B):
        # write code here
        '''
        参考题解：
        链接：https://www.nowcoder.com/questionTerminal/e7e0d226f1e84ba7ab8b28efc6e1aebc
来源：牛客网

        二进制加法。发现一个特点。
        位的异或运算跟求'和'的结果一致：
        异或 1^1=0 1^0=1 0^0=0     
        求和 1+1=0 1+0=1 0+0=0
        位的与运算跟求'进位‘的结果一致：
        位与 1&1=1 1&0=0 0&0=0
        进位 1+1=1 1+0=0 0+0=0
        于是可以用异或运算和与运算来表示加法

        public int addAB(int A, int B) {
            int xor,and;
            while(B!=0){
                xor = A^B;
                and = (A&B)<<1;
                A=xor;
                B=and;
            }
            return A;
         }

        '''
        while B!=0:
            bit_xor = A^B
            bit_and = (A&B)<<1
            A = bit_xor
            B = bit_and
        return A