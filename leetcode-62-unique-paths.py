'''
leetcode-62-unique-paths.py
不同路径
https://leetcode-cn.com/problems/unique-paths/

#
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？
'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        '''
        思路二：
        在思路一的基础上压缩空间，一位数组，一行一行的计算，直到最后一个，搞定
        https://blog.csdn.net/zw159357/article/details/81208596
        '''
        
        
        '''
        思路一:
        典型dp问题；

        
        #=====
        S 1 1 1 1 1
        1 2 3 4 5 6
        1 3 6 
        1 4 
        1 5
        1 6
        #=====
        
        对于矩阵(s为起点)
        Start A B C 1
            D E F G 2
            H I J K End
        中的A点，用 dp[0][1]表示从起点S到A的不同路径数目；
        f(A) = dp[0][1] = 1 , f(B) = dp[0][2] = 2,
        f(D) = dp[1][0] = 1 , f(H) = dp[2][0] = 2,
        
        f(E) = f(A)+f(D) = 2;
        f(x) = f(x左) + f(x右)
        
        通式：
            dp[i][j] = i|j  if i&j==0
                     = dp[i-1][j] + dp[i][j-1]
            可看出对称属性，即 dp[i][j] = dp[j][i]
        '''
        #正向非递归==》动态规划
        #保证行小于列 ;例如3,5
        m,n = [n,m] if m>n else [m,n]
        dp=[[1 for i in range(n)] for i in range(m)]
        i = 1
        while i<m:
            # 可看出对称属性，即 dp[i][j] = dp[j][i]
            #所以只计算其中一部分
            #i=j的时候,dp[i][i]等于其正上方的值的两倍（因为对称）
            dp[i][i] = 2*dp[i-1][i]
            j = i+1
            while j<n:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
                j+=1
            i+=1
        return dp[m-1][n-1]
        
        #递归
        def f(i,j):
            if i==0 or j==0: return 1
            #if i&j==0: return 1 #错误,因为 2&1 也等于0
            return f(i,j-1)+f(i-1,j)
        return f(m-1,n-1)