'''

 x 的平方根
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去
'''


class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        使用牛顿法迭代逼近求解
        x(n+1) = x(n) - f( x(n) )/{f( x(n) )对x的导数}；其中y为定值，由题目指定
        优化目标函数（损失函数）：min  (x^2 - y)  ； s.t.x∈R 此函数错误。。。？
        或
        优化目标函数（损失函数）：min  0.5*(y - x^2)^2 ； s.t.x∈R，对x求导=-2*x*(y-x^2)
        x 为待求解的目标值;y 为给定的数，满足 x^2 = y
        '''
        y = x
        x = 1 #初始值
        #f(x)除以f(x)的导数
        def f_div_f_d(x_n,y):
            #{f( x(n) )的导数} = (0.5*(y - x^2)^2)' = -2.0*x*(y-x^2), 其中y为定值，由题目指定
            #print('f_div_f_d:  step=',(0.5*(y - x_n**2)**2) / (-2.0*x_n*(y-x_n**2)))
            return (0.5*(y - x_n**2)**2) / (-2.0*x_n*(y-x_n**2))
        
        #判断是否满足精度
        def satisfy_precision(x_n,y):
            #print('satisfy_precision: ',(int(x_n))**2,(int(x_n)+1)**2)

            if y >= (int(x_n))**2 and y < (int(x_n)+1)**2:
                return 1
            else: return 0
        
        while( satisfy_precision(x,y) == 0):
            #x(n+1) = x(n) - f( x(n) )/{f( x(n) )对x的导数}；其中y为定值，由题目指定
            x = x - f_div_f_d(x,y)
            #print('while:  x=',x)
            
        return int(x)

if __name__ == '__main__':
    tmp = Solution()
    res = tmp.mySqrt(9)
    print(res)