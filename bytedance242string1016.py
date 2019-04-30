'''
kmp算法
'''
class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        i=0
        s1Cpy = s1
        startCmp=-1
        while i<len(s2):
            
            indx = s1Cpy.find(s2[i])
            if indx == -1:
                #not find
                if s1.find(s2[i]) != -1:
                    #s1 cunzai,cexiao caozuo                    
                    #assert: last != -1
                    lastD = s2.find(s2[i],startCmp)
                    s1Cpy = s1
                    for a in s2[lastD+1:i+1]:
                        s1Cpy = s1Cpy.replace(a,"",1)
                    startCmp = lastD+1
                else:
                    #s2[i] buzai s1 zhong
                    s1Cpy = s1
                    startCmp = -1
                
            else:
                #find
                startCmp = i if startCmp == -1 else startCmp
                s1Cpy = s1Cpy.replace(s2[i],"",1)
                if len(s1Cpy) == 0:
                    return True
            
            i+=1
        return False


def main():
    mycls = Solution()
    res = mycls.checkInclusion(s1="adc",s2="dcda")

    print(res)

if __name__ == '__main__':
    
    x = "  hello Tom  i m here  "
    lx = x.split()
    print(lx)
    #main()
