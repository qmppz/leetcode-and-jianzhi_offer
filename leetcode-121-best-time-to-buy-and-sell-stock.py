'''
leetcode-121-best-time-to-buy-and-sell-stock.py
买卖股票的最佳时机
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''

class Solution:
    def maxProfit(self, prices: list) -> int:
        '''
        思路三：
        https://blog.csdn.net/ChenVast/article/details/78950392
        参考解法：时间O(n)，空间O(1)
        该题解法和最大连续子数组和的解法思路是一样的；只需遍历一次数组
        
        注意理解几个例子：
        [1,2,3,4,5] 如果从第一天开始，一直重复操作【当天买入，明天全部卖出】；那么
        max_profit = 【2-1】+【3-2】+【4-3】+【5-4】 = 4
        和直接第五天卖出的结果相同【5-1】= 4
        所以使用临时利润 tmp_profit 累计相邻天数的利润
        
        
        '''
        
        max_profit, tmp_profit = 0, 0
        for pi in range(len(prices)-1):
            #当前价格序列走势上升或下降
            up_or_down = prices[pi+1] - prices[pi]
            print("up_or_down",up_or_down,tmp_profit,max_profit)
            if up_or_down>=0: 
                tmp_profit += up_or_down
            else: 
                #最多只允许完成一笔交易
                max_profit = max(max_profit, tmp_profit)
                #临时利润 tmp_profit 如果还能抵扣当前 prices[pi+1] - prices[pi] 的亏损；那么就承担这次亏损，而不是直接清零
                # 比如[1,5,3,8];5 和 3那里产生了亏损，但是由于之前【5-1】盈利大于这次亏损，那么就继续执行 【当天买入，明天全部卖出】的操作；
                if tmp_profit+up_or_down>=0:
                    tmp_profit += up_or_down  
                else:
                    #临时利润 tmp_profit 承担不了，说明遇到了更低的买入价格，此时应该从新开局，买入；
                    tmp_profit = 0
        return max(max_profit, tmp_profit)
    
        '''
        思路一： 超时
        举例：[2,7,1,4,5]; max_profit = max{7-2, 5-1}
        [4,7,1,4,6] ; max_profit = max{7-4, 6-1}
        即每次寻找数组中的最大数的坐标 max_idx，由此截断为两部分；在前部分中寻找最小值，获取候选答案tmp_profit = 最大值-最小值；
        然后对截断的后部分做同样的操作；直到后部分的长度小于2为止
        
        max_profit = 0
        while len(prices)>=2:
            max_idx = 0
            for p in range(len(prices)):
                if prices[max_idx] < prices[p]: max_idx = p
            
            if max_idx == 0: prices = prices[max_idx+1:] ; continue
            
            min_idx = 0
            for p in range(max_idx):
                if prices[min_idx] > prices[p]: min_idx = p

            max_profit = max(max_profit, prices[max_idx]-prices[min_idx])
            prices = prices[max_idx+1:]
        return max_profit
        '''
        '''
        思路二：两层for循环，找最大差值
        超时
        
        max_profit=0
        for i in range(len(prices)):
            for k in range(i+1,len(prices)):
                max_profit = max(max_profit, prices[k] - prices[i])
        return max_profit
        '''
        
        '''
def main():
    mycls = Solution()
    res = mycls.maxProfit(prices=[2,1,2,0,1])

    print(res)

if __name__ == '__main__':
    main()
        '''