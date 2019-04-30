'''
jianzhi offer - 二维数组中的查找
https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e?tpId=13&tqId=11154&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        '''
        #方法一
        T=O(N logN)
        先对最后一列进行判断，大于target时，该行才可能存在该数；
        然后对矩阵的满足上述条件的行进行二分查找
        
        n, m = len(array), len(array[0])
        if n==0 or m == 0: return False
        
        for elist in array:
            if elist[-1]<target or elist[0]>target: continue
            l, r = 0, len(elist)-1
            while l<=r:
                mid = (l+r)//2
                if elist[mid] == target:
                    return True
                if elist[mid] > target:
                    r = mid - 1
                else: l =  mid + 1
        return False
        '''
        #--------------------------------------
        '''
        从左下 搜索 到 右上，T=O(N+M)
         * 利用二维数组由上到下，由左到右递增的规律，
         * 那么选取左下角或者右上角的元素a[i][j]与target进行比较，
         * 当target大于元素a[i][j]时，那么target必定在元素a所在行的右边,
         * 即j++；
         * 当target大于元素a[i][j]时，那么target必定在元素a所在列的上边,
         * 即i--；
         * 时间复杂度m+n
        '''
        n, m = len(array), len(array[0])
        if n==0 or m == 0: return False
        
        i, j = n-1, 0
        while i>=0 and j<m:
            if array[i][j]<target: j+=1
            elif array[i][j]>target: i-=1
            else: return True
        return False
    #----------------------
    '''
    方法三， 左上角与右下角 递增关系，则可递归的调用二分
    时间复杂度 T=O(N logN)
    '''