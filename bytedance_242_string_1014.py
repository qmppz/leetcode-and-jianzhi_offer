class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #baseline
        i=0
        res=""
        if len(strs)<1:
            return ""
        import sys
        while i<sys.maxsize: 
            
            j=0
            while j<len(strs):
                if len(strs[j])<=i:
                    return res
                    
                if strs[0][i] != strs[j][i]:
                    return res
                    
                j+=1
            res+=strs[0][i]
            i+=1
            


def main():
    mycls = Solution()
    res = mycls.longestCommonPrefix(strs=["qwe"])

    print(res)

if __name__ == '__main__':
    main()