'''
leetcode-169-majority-element.py
求众数
https://leetcode-cn.com/problems/majority-element/

#
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

#参考题解：https://blog.csdn.net/z983002710/article/details/81164777
摩尔投票法
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        思路一：T=O(N),S=O(1)
        摩尔投票法
        根据题目定义 【众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素】
        n=5时，出现次数需要大于等于  5//2 + 1 = 3 次
        n=6时，出现次数需要大于等于  6//2 + 1 = 4 次
        
        众数必出现超过数组的一半
        用一个计数器zs_cnt,遍历一次数组，当前元素等于上一个元素 则加一，不等则减一
        如果存在众数的话 ，zs_cnt 最终结果必定大于等于1，
        【1,1,1,1,2,3,4】 【1,2,1,3,1,4,1】
        [1,1,1,2,2]
        '''
        zs_cnt = 1
        zhongshu = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == zhongshu: 
                #当前的数等于之前记录的zhongshu，计数器加一
                zs_cnt += 1 
            else: 
                #当计数器减为0，说明之前记录的zhongshu有可能不是真的众数；所以重新给zhongshu赋值，初始化计数器
                zs_cnt -= 1 
                if zs_cnt <= 0:
                    zs_cnt = 1
                    zhongshu = nums[i]
        return zhongshu
        
        
        
        
        
        
        