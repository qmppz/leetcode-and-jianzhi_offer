class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        #BFS
        x, y, n, ans = 0, 0, 0, 0
        groupSet = set()
        while n < len(M):
            if M[n][n] == 1:
                ans += 1
                groupSet.add(n)
                while groupSet:
                    ni = groupSet.pop()
                    M[ni][ni] = 0
                    i = 0
                    while i < len(M):
                        if M[ni][i] == 1 and M[i][i] == 1:
                            groupSet.add(i)
                        i += 1
            n+=1
        return ans


def main():
    mycls = Solution()
    res = mycls.findCircleNum(M=[[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])

    print(res)

if __name__ == '__main__':
    main()
