'''
jianzhi-offer-顺时针打印矩阵
https://www.nowcoder.com/practice/9b4c81a02cd34f76be2659fa0d54342a?tpId=13&tqId=11172&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''


# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        '''
        硬搞法
        定义当前遍历前进的方向 orien= 0右  1下  2左  3上
        定义数组的边界 edge={'right': col, 'down':row, 'left':0,'up':0}
        cnt问计数，统计打印的数字
        '''
        #判断x y是否越界
        def valid(x,y,edge):
            #row
            if x>edge['down']: return 'down-error'
            if x<edge['up']: return 'up-error'
            #col
            if y>edge['right']: return 'right-error'
            if y<edge['left']: return 'left-error'
            return 'valid'
        
        if not matrix or not matrix[0] : return  
        row, col = len(matrix)-1, len(matrix[0])-1
        orien=0
        edge={'right': col, 'down':row, 'left':0,'up':0}
        cnt=0
        resList=[]
        x,y=0,0
        while cnt<(row+1)*(col+1):
            status = valid(x,y,edge)
            if status == 'valid':
                resList.append(matrix[x][y])
                cnt+=1
                if orien==0: y+=1
                elif orien==1: x+=1
                elif orien==2: y-=1
                else: x-=1
            else:
                if status == 'down-error':
                    x-=1
                    y-=1
                    orien=2
                    edge['right']-=1
                elif status == 'up-error':
                    x+=1
                    y+=1
                    orien=0
                    edge['left']+=1
                elif status == 'right-error':
                    y-=1
                    x+=1
                    orien=1
                    edge['up']+=1
                else:
                    y+=1
                    x-=1
                    orien=3
                    edge['down']-=1
        return resList
        
        