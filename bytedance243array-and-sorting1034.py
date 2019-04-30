
#baseline
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        direction = [[-1,0],[1,0],[0,-1],[0,1]]
        maxArea = 0
        XLEN, YLEN = len(grid), len(grid[0])
        i=0
        while i<XLEN:
            j=0
            while j<YLEN:
                if grid[i][j] == 1:
                    queueSet = set()
                    queueSet.add(str(i)+"-"+str(j))
                    islandArea = 0
                    while queueSet:
                        coordinate = queueSet.pop().split("-")
                        x,y = int(coordinate[0]),int(coordinate[1])
                        islandArea += 1 
                        grid[x][y] = 0
                        for d in direction:
                            dx,dy = x+d[0],y+d[1]
                            if dx>=0 and dy>=0 and dx<XLEN and dy<YLEN and grid[dx][dy] == 1:
                                queueSet.add(str(dx)+"-"+str(dy))
                    maxArea = max(maxArea,islandArea)
                j+=1
            i+=1
        return maxArea



def main():
    mycls = Solution()
    res = mycls.maxAreaOfIsland(grid=[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,1,0,0,0,0],
 [0,0,0,0,0,1,0,0,1,0,1,0,0],
 [0,1,0,1,1,1,0,0,0,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,1,0,0,1,1,1,1,0,1],
 [1,0,0,0,0,0,0,1,1,0,0,0,1]])

    print(res)

if __name__ == '__main__':
    main()
    q2 = [1,2,3,4,5]
    q = q2
    print(q,q2)
    q[0] = -999
    print(q,q2)
    q2[0] = +1000
    print(q,q2)
    