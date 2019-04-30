'''
https://www.acwing.com/problem/content/submission/61/
---
在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。

输入一个数组，求出这个数组中的逆序对的总数。

样例
输入：[1,2,3,4,5,6,0]

输出：6
---

参考题解：https://blog.csdn.net/Lynette_bb/article/details/75581325
归并排序最优解法：https://www.nowcoder.com/profile/6526467/codeBookDetail?submissionId=44116979
'''



class Solution(object):
    def inversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        #方法一 
        T=O(N^2)
        '''
        '''
        
        from sys import maxint
        delidx=[]
        cnt=0
        while len(delidx)<len(nums):
            idx = nums.index(min(nums))
            delidx.append(idx)
            nums[idx]=maxint
            
            delnum=0
            for e in delidx:
                if e<idx:delnum+=1
            cnt+=idx-delnum
    
        return cnt
        '''
        
        