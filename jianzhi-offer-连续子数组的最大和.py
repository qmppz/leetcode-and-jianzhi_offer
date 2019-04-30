'''
jianzhi-offer-连续子数组的最大和
https://www.nowcoder.com/practice/459bd355da1549fa8a49e350bf3df484?tpId=13&tqId=11183&rp=3&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tPage=2


题目描述
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
'''

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        '''
        思路一：
        tmp_sum 临时累加和：表示某一段连续的数的累加和
        
        遍历array，每次更新 tmp_sum，当tmp_sum为负时，则记录tmp_sum为负之前的最大值，然后tmp_sum初始化为0 重新累加
        注意array末尾负数的情况，所以先去除收尾负数
        '''
        s=-1
        e=-1
        for i in range(len(array)):
            if array[i]>0:
                s=i
                break
        for i in range(len(array)-1,s,-1):
            if array[i]>0:
                e=i
                break
        if s==-1 or e==-1:return max(array)
        array=array[s:e+1]
        
        tmp_sum=array[0]
        max_tmp_sum=array[0]
        for num in array[1:]:
            if num+tmp_sum>=0:
                tmp_sum += num
            else:
                max_tmp_sum = max(max_tmp_sum, tmp_sum)
                tmp_sum = 0
        return max(max_tmp_sum, tmp_sum)
        