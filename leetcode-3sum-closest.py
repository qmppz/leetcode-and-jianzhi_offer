'''
leetcode-3sum-closest.py
最接近的三数之和
https://leetcode-cn.com/problems/3sum-closest/

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        '''
        思路一：排序，然后三层for循环
        思路二：排序，然后两层for循环，在第二层中用二分查找返回 与第三个数距离最小的数
        思路三：排序，然后两层for循环，
        参考：https://blog.csdn.net/jaster_wisdom/article/details/80468931
        我们可以想到一种时间复杂度为O(n^2)的解法：假设数组中有len个元素，首先我们将数组中的元素按照从小到大的顺序进行排序。其假设取的第一个数是A[i]，那么第二三两个数从A[i+1]~A[len]中取出。找到“第一个数为A[i]固定，后两个数在A[i]后面元素中取。并且三数之和离target最近的情况。”
        这时，第二层循环我们用两个指针j,k分别指向A[i+1]和A[len]，
        如果此时三数之和A[i]+A[j]+A[k]<target，说明三数之和小了，我们将j后移一格；
        反之，若和大于target，则将k前移一格；
        直到j和k相遇为止。
        在这期间，保留与target最近的三数之和。一旦发现有“和等于target的情况”,立即输出即可。
        '''
        if len(nums)<3: return 0
        nums.sort()
        min_sum=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-1):
            #左右指针
            l, r = i+1, len(nums)-1
            while l != r:
                tmp_sum = nums[i]+nums[l]+nums[r]
                if tmp_sum == target: return tmp_sum
                if abs(target-min_sum) > abs(target-tmp_sum): min_sum = tmp_sum 
                
                if tmp_sum < target: l+=1
                else: r-=1
        return min_sum
        