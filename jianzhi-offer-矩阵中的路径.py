# -*- coding:utf-8 -*-
'''
jianzhi-offer-矩阵中的路径.py
https://www.nowcoder.com/practice/c61c6999eecb4b8f88a98f66b273a3cc?tpId=13&tqId=11218&rp=4&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tPage=4

题目描述
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
'''


class Solution:
    #def hasPath(self, matrix,path):
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        '''
        a b c e 
        s f c s 
        a d e e 
        
        包含一条字符串"bcced"的路径
        不包含"abcb"路径
        
        如果题目不要求寻找的路径有序，乱序也可以的话，思路一：
        
        判断是否包含某字符串path，可先用hash表保存这个path串，
        借鉴【最小覆盖子串】里面判断是否包含某个串的思想https://blog.csdn.net/qq_41231926/article/details/81427851
        
        使用 hashtable 保存path的每个字符出现的次数；
        count表示被查看的字符的数量，当count == len(path)那么表示全部被查看
        count 只有 在hashtable(ch) >0 的时候才会+1，且此时hashtable(ch)也要同时-1
        
        '''
        '''
        正确思路一： 回溯法
        用栈保存path串，
        
        '''
        if not matrix : return False
        #rows, cols = len(matrix), len(matrix[0])
        #xy坐标自动转换
        def xy2Sstr(ele):
            SPLITCHAR = '|'
            return str(ele[0])+SPLITCHAR+str(ele[1]) if isinstance(ele, list) else [int(e) for e in ele.split(SPLITCHAR)]
        
        def judge_path(x,y,idx_path,trace_xy_set):
            #print("x",x,"y",y,"s[i]",path[idx_path],"?",matrix[x][y],"set",trace_xy_set)
            '''
            idx_str： path字符串的指针，从第一个往后遍历
            trace_xy_set： 当前路径，便利过的字符集合
            查找 当前x,y 点是否满足  等于 path[idx_path]且不在trace_xy_set中（没有被访问）
            
            注意set为可变类型，作为形参传递的是地址，所以这里需要深度复制
            '''
            #当前点不等则返回false
            #if matrix[x*cols+y] != path[idx_path]:
            if matrix[x][y] != path[idx_path]:
                return False
            #print("√")
            #当前点相等
            if len(path)-1 == idx_path: return True
            #当前点被访问
            trace_xy_set.add(xy2Sstr([x,y]))
            #idx+1
            idx_path += 1
            
            # 当前点的四个方向
            four_direction = [[x-1, y],[x+1, y],[x,y-1],[x,y+1]]
            for x, y in four_direction:
                if x>=0 and y>=0 and x<rows and y<cols and xy2Sstr([x,y]) not in trace_xy_set:
                    #注意set为可变类型，作为形参传递的是地址，所以这里需要深度复制
                    trace_xy_set_copy = set(trace_xy_set)
                    if judge_path(x,y,idx_path,trace_xy_set_copy) == True:
                        return True
            return False
        
        #将一维 matrix 转为 二维
        matrix = [list(matrix[_row*cols:(_row+1)*cols ]) for _row in range(0,rows)]
        
        for x in range(rows):
            for y in range(cols):
                if judge_path(x,y,0,set()) == True : return True
        return False
'''
c = Solution()
res = c.hasPath([
["D", "G", "A", "J", "A", "N"], 
["W", "U", "U", "Z", "E", "Q"], 
["I", "F", "M", "M", "G", "B"], 
["Y", "Y", "E", "M", "D", "K"], 
["M", "F", "S", "N", "H", "O"]],"GAUZEGDK")
print(res)

[
["D", "G", "A", "J", "A", "N"], 
["W", "U", "U", "Z", "E", "Q"], 
["I", "F", "M", "M", "G", "B"], 
["Y", "Y", "E", "M", "D", "K"], 
["M", "F", "S", "N", "H", "O"]]
"GAUZEGDK"
'''

