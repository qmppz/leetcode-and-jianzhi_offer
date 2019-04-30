'''
jianzhi-offer-机器人的运动范围.py
https://www.nowcoder.com/practice/6e5207314b5241fb83f2329e89fdecc8?tpId=13&tqId=11219&tPage=4&rp=4&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking



题目描述
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''


# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        '''
        思路一：BFS，统计格子数 不可行
        '''
        '''
        思路二： 回溯法：DFS/BFS + 剪枝
        '''
        # BFS 版本
        
        #特例判断
        if threshold<0 or rows<0 or cols<0 : return 0
        
        global coordinate_visited
        #xy坐标自动转换
        def xy2Sstr(ele):
            SPLITCHAR = '|'
            return str(ele[0])+SPLITCHAR+str(ele[1]) if isinstance(ele, list) else [int(e) for e in ele.split(SPLITCHAR)]
            
        #判断xy是否可行
        def valid(xy_list):
            #Python3.0中新增的关键字，python2.x不支持；指当前的这个变量不是局部变量
            #nonlocal coordinate_visited
            #python 2.7 中使用global
            global coordinate_visited
            x, y = xy_list
            if xy2Sstr(xy_list) not in coordinate_visited and x<rows and y<cols and x>=0 and y>=0 :
                sum_single = 0
                while x>0 or y>0:
                    sum_single += x%10 + y%10
                    x //= 10 ; y //= 10
                if sum_single <= threshold : return True
            return False
            
        coordinate_buffer = {xy2Sstr([0,0])}
        coordinate_visited = set()
        while len(coordinate_buffer)>0:
            x, y = xy2Sstr(coordinate_buffer.pop())
            #print(x,y)
            #默认 buffer里面的都是有效的，如果重复，set集合也会自动处理
            coordinate_visited.add(xy2Sstr([x,y]))
            #从 0 0 开始，所以只往右、下递增判断即可
            #加入之前判断是否有效
            coordinate_buffer.add(xy2Sstr([x+1,y])) if valid([x+1,y])==True else None
            coordinate_buffer.add(xy2Sstr([x,y+1])) if valid([x,y+1])==True else None
            
        return len(coordinate_visited)

'''
c = Solution()
res = c.movingCount(4,4,4)

print(res) if 1==1 else None
'''