'''
jianzhi-offer-数组中重复的数字.py
https://www.nowcoder.com/practice/623a5ac0ea5b4e5f95552655361ae0a8?tpId=13&tqId=11203&rp=2&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tPage=3


题目描述
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
示例1
'''

# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        '''
        思路一：T=O(N) S=O(1)
        根据题目意思“所有数字都在0到n-1的范围内”，将numbers中的数看做坐标，
        遍历每个坐标，将numbers[numbers[i]]的值变为负数，表示这个位置已经被操作，
        比如 0，1,3,2,3， i从0开始计数
        第一次循环变为,0，-1,3,2,3
        二,0，-1,3,-2，3#操作第二个数【3】，即将numbers[3]对应的值变为负数，表示坐标3已经出现过了
        三,0，-1,-3，-2，3#操作第三个数【2】，将numbers[2]对应的数变为负数，表示坐标2已经出现过了
        四,0，-1，-3,-2,3#操作第四个数【3】，此时发现 numbers[3]值已经为负，所以重复
        
     
        '''
        for i in range(len(numbers)):
            idx = abs(numbers[i])
            if numbers[idx] < 0:
                #已经被操作过了，重复
                duplication[0]=idx
                return True
            else: numbers[idx] *=-1
        return False
        