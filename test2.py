
'''
0-1背包问题
http://hihocoder.com/problemset/problem/1038?sid=770359

'''
import sys

if __name__ == '__main__':

    line = sys.stdin.readline().strip()
    N, M = [e for e in map(int, line.split())]
    need=[0]
    value=[0]
    for i in range(N):
        _need, _value = [e for e in map(int, sys.stdin.readline().strip().split())]
        need.append(_need)
        value.append(_value)

    #基础解法: dp[i][j] 表示总容量为j的限制下，扫描到第i个物品是的最优值（i从1开始）
    #dp[i][j] = dp[i-1][j] if need[i] > j else max(dp[i-1][j-need[i]]+value[i],dp[i-1][j])
    
    dp=[[0]*(N+1)]*(M+1)
    print(dp)
    for i in range(1,N+1):
        
        for j in range(1,M+1):
            dp[i][j] = dp[i-1][j] if need[i] > j else max(dp[i-1][j-need[i]]+value[i],dp[i-1][j])
    
    print(dp[N][M])
  
    
    
    
    
    