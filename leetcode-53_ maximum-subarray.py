class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        https://leetcode-cn.com/problems/maximum-subarray/
        给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

        示例:

        输入: [-2,1,-3,4,-1,2,1,-5,4],
        输出: 6
        解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
        '''
        '''
        #方法一
        #时间效率O(N^2) 
        #给定起点和终点，判断之间的组合sum
        private int max = Integer.MIN_VALUE;
        public int maxSubArray(int[] nums) {
            int sum;
            for (int i = 0; i < nums.length; i++) {// 子序列左端点
                sum = 0;
                for (int j = i; j < nums.length; j++) {// 子序列右端点
                    sum += nums[j];// 这里就相当于每次根据前一次的序列来计算新的序列
                    if (sum > max)
                        max = sum;
                }
            }
            return max;
        }

        '''
        #方法2
        '''
        #时间复杂度O(N)
        思路：[-2,1,-3,4,-1,2,1,-5,4]
        最大连续子序列和应该从某各正数开始（如果全为负就返回最大的负数）
        定义maxSum ,sum;从第一个元素开始，当sum累加为负值则重置为0，重新累加，如果为正则判断与maxSum的大小
        '''
        
        sum = 0 if nums[0]<0 else nums[0]
        #先取最大值
        maxSum = max(nums)
        for e in nums[1:]:
            #当前元素<0，sum先累加，在判断sum的正负情况，
            sum+=e  
            if sum<0:
                #此时sum也小于0的话，那么就没有再往后累加的意义，负数对任何值求和都是对对方的削弱
                sum=0
            else:
                #sum>0,若大于maxSum则更新maxSum的值
                maxSum=max(maxSum,sum)
            
        return maxSum
            
            
        