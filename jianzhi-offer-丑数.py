'''
jianzhi-offer-丑数.py
https://www.nowcoder.com/practice/6aa9e04fc3794f68acf8778237ba065b?tpId=13&tqId=11186&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

'''
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        '''
        思路一：对每一个数都判断是否为丑数效率太低，判断了很多没有意义的数
        暴力顺序求解，挨个判断是不是丑数
        构建 factor=set(),将丑数放入其中,在判断一个数num是否为丑数时，
        根据丑数定义，丑数必定能被2,3,5整除，所以
        取num的一对包含2、3或5的因子，判断是否在factor里面即可，若不在或没有除了1和num本身的因子，则不是丑数
        
        
        #定义函数，获取任意一对除了1和num本身的因子,不存在则num为质数，返回[-1,-1]
        def get_factor(num):
            for dv in [2,3,5]:#range(2,int(num**0.5)):
                if num%dv==0:
                    return [dv,num//dv]
            return [-1,-1]
        
        factor_set = set([1,2,3,4,5,6,8,9])
        if index<9:return [1,2,3,4,5,6,8,9][index-1]
        start = 10
        cnt=9
        num=10
        print(index)
        while cnt<=index:
            a, b = get_factor(num)
            if b in factor_set:
                factor_set.add(num)
            cnt = len(factor_set)
            num+=1
        return max(factor_set)
        '''
        '''
        思路二：
        跳跃记录2,3,5组合的乘积值，不直接遍历每一个数
        2,3,5组合乘积得的值必定为丑数；
        定义 ugly_list = [1,2,3,4,5,6]
        为基础因子[2,3,5]定义指针 idx_2,idx_3,idx_5
        
        循环直到len(ugly_list) == index为止
        每次循环 在ugly_list[ idx_2,idx_3,idx_5]*2 3 5中找最小的值，ugly_list
        题解：https://www.nowcoder.com/questionTerminal/6aa9e04fc3794f68acf8778237ba065b
        
        '''
        ugly_list = [1,2,3,4,5]
        idx_2,idx_3,idx_5 = 2,2,2
        if index<6:return ugly_list[index-1] if index>0 else 0
        while len(ugly_list)<index:
            min_num = min(ugly_list[idx_2]*2, ugly_list[idx_3]*3, ugly_list[idx_5]*5)
            if min_num == ugly_list[idx_2]*2: idx_2 += 1
            if min_num == ugly_list[idx_3]*3: idx_3 += 1
            if min_num == ugly_list[idx_5]*5: idx_5 += 1
            ugly_list.append(min_num)
        return ugly_list[-1]
            
            
        
        