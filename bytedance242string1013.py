class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        import re
        path = re.sub(r"/{2,}","/",path)
        path = re.sub(r"(/\.(?=\/))","",path)
        if path[-1] == "/":
            path = path[:-1]
        while(path[-2:] == "/."):
            path = path[:-2]
        
        pathList = path.split("/")[1:]
        backStep = 0
        i=len(pathList)-1
        while i>=0:
            if pathList[i] == "..":
                pathList.pop(i)
                backStep+=1
                
            else:
                if backStep>0:
                    pathList.pop(i)
                    backStep-=1
            i-=1
        return "/"+"/".join(pathList)



def main():
    mycls = Solution()
    res = mycls.simplifyPath(path="/.//a////b/../c/./.././d")

    print(res)

if __name__ == '__main__':
    

    main()
