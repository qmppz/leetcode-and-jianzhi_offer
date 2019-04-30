class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        '''
        f(ai) = 1 if idx == 0
              = max( {f(ai-1)+1|ai坐标完全>ai-1坐标}U{f(ai-1)|ai坐标不完全>ai-1坐标}
        '''
        if len(envelopes) < 2: return len(envelopes)
        envelopes.sort(key=lambda interval:interval[0])
        dictM = {0:[envelopes[0]]}
        lastNum = envelopes[0][0] 
        i=1 ; idx = 0  
        while i<len(envelopes):
            if envelopes[i][0] == lastNum:
                dictM[idx].append(envelopes[i])
            else:
                idx += 1
                dictM[idx] = [envelopes[i]]
                lastNum = envelopes[i][0]
            i += 1
        f = {i:[1]*len(dictM[i]) for i in range(idx+1)}
        i=1
        while i<idx+1:
            j=0
            while j<len(dictM[i]):
                maxE = 0
                k=0
                while k<len(dictM[i-1]):
                    e = dictM[i-1][k]
                    if e[0]<dictM[i][j][0] and e[1]<dictM[i][j][1]:
                        maxE = max(maxE,f[i-1][k]+1)
                    else:
                        maxE = max(maxE,f[i-1][k])
                    k += 1
                f[i][j] = maxE
                j += 1
            i += 1
        print(dictM,"\n",f)
        return max(f[idx])

def main():
    mycls = Solution()
    res = mycls.maxEnvelopes(envelopes = [[1,3],[3,5],[6,7],[6,8],[8,4]])
    print(res)

if __name__ == '__main__':
    main()
