'''
leetcode-merge-sorted-array.py
合并两个有序数组
https://leetcode-cn.com/problems/merge-sorted-array/

#
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        '''
        思路一：T=O(N) S=O(1)
        从后往前遍历，指向nums1 中下一个空位的指针 next_blank
        指向nums1 下一个待比较的数 next_n1, 
        指向nums2 下一个待比较的数 next_n2, 
        每次比较 next_n1 与 next_n2 的值的大小，大的放后面；
        直到 next_n2 为0 为止
        
        '''
        next_blank = len(nums1)-1
        next_n1, next_n2 = m-1, n-1
        
        while next_n2 >= 0 :
            if next_n1 >= 0 and nums1[next_n1] > nums2[next_n2] : 
                nums1[next_blank] = nums1[next_n1]
                next_n1 -= 1
            else :
                nums1[next_blank] = nums2[next_n2]
                next_n2 -= 1
            next_blank -= 1
        # list 同步修改，不需要返回
        return ;
