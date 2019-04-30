'''
jianzhi-offer-和为S的两个数字
https://www.nowcoder.com/practice/390da4f7a00f44bea7c2f3d19491311b?tpId=13&tqId=11195&tPage=3&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出。
'''

# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        '''
        思路一：
        dict储存array，从 array[0] 到 array[i], 其中array[i]<tsum//2， 判断是否存在一对加起来等于tsum
        乘积最小，即两个数相差最大时，乘积最小，取第一个满足的数对即可
        
        '''
        dict_arr={}
        res=[]
        for e in array:
            #不存在则创建，并赋值为1
            dict_arr[str(e)] = dict_arr.get(str(e),0)+1
            
        for e in [i for i in array if i <= tsum//2]:
            another_num = tsum-e
            if str(another_num) in dict_arr:
                res=[e,another_num]
                break
        if len(res)==0 and tsum%2==0 and tsum//2 in dict_arr and dict_arr[tsum//2]>=2:
            res = [tsum//2,tsum//2]
        
        return res
        
        