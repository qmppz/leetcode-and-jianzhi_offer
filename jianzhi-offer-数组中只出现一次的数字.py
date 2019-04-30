'''
jianzhi-offer-数组中只出现一次的数字.py
https://www.nowcoder.com/practice/e02fdb54d7524710a7d664d082bb7811?tpId=13&tqId=11193&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


题目描述
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''

# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        '''
        思路一：位运算法，由性质： a^b^c=a^(b^c)=(a^c)^b
        
    (1)对于出现两次的元素，使用“异或”操作后结果肯定为0，那么我们就可以遍历一遍数组，对所有元素使用异或操作，那么得到的结果 yihuo 就是两个出现一次的元素的异或结果。

    (2)因为这两个元素不相等，所以异或的结果肯定不是0，也就是可以再异或的结果中找到1位不为0的位，例如异或结果的最后一位不为0。

    (3)这样我们就可以最后一位将原数组元素分为两组，一组该位为1，另一组该位为0。
    也就是说，对于 yihuo 这个值的二进制中某一位值为1 的位来说，一定是由0 ^ 1 得来
    例如：yihuo 的二进制：....0010 倒数第二位为1，由于1只能通过 1 疑惑 0 得来，
    所以这个 倒数第二位的1 一定来自于某两个数：......1. 和......0.；所以可将array中的数分为两类
    分别求累计异或，得到的两个数就是答案，

    (4)再次遍历原数组，最后一位为0的一起异或，最后一位为1的一起异或，两组异或的结果分别对应着两个结果。
        
        '''
        if len(array)<=2: return array
        yihuo = 0# 0 ^ x = x
        for e in array:
            yihuo ^= e
        #移位寻找 yihuo 二进制中 值一位为1 的位
        index=1
        for i in range(1,33):
            if (yihuo >> i)&1 == 1: index=i; break;
                
        #将array分为两类，分别累计异或
        res_a, res_b = 0, 0
        for e in array:
            if e >> index & 1 == 1: 
                res_a ^= e
            else:
                res_b ^= e
                
        return res_a, res_b
                
                
            
            
        
        
        