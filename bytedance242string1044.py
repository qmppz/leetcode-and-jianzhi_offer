
class Solution:

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        return self.searchIp(1,[],s)
        
    def searchIp(self,c,lastPart,s):
        sLen = len(s)

        if c == 4 :
            num = int(s)
            if (num<=255 and s[0] != '0') or (s[0]=='0'and sLen==1):
                lastPartCpy = lastPart.copy()
                lastPartCpy.append(s)#append没有返回值 ，即返回none
                return [".".join(lastPartCpy)]
            else:
                return []
        else:
            i=1
            ansList=[]
            while i<4: 
                currentNumStr = s[:i]
                if sLen-i >= 4-c and sLen-i<=3*(4-c) and int(currentNumStr)<=255:
                    #vaild
                    lastPartCpy = lastPart.copy()
                    lastPartCpy.append(currentNumStr) #append没有返回值 ，即返回none
                    ans = self.searchIp(c+1,lastPartCpy,s[i:])
                    
                    if len(ans)>0:
                         ansList+=ans
                    if currentNumStr[0] == '0':
                        break 

                i+=1

            return ansList


def main():
    mycls = Solution()
    res = mycls.restoreIpAddresses(s="1011101010")

    print(res)

if __name__ == '__main__':
    main()
 
 