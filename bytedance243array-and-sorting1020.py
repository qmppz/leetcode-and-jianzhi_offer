#coding:utf-8
#模板https://github.com/luliyucoordinate/Leetcode/blob/master/src/0015-3Sum/0015.py
#T=1148ms
class Solution:
            
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numsLen = len(nums)
        if numsLen < 3:
            return []
        ansList=[]
        dictRepeat = {}
        numsP = []
        numsN = []
        i=0
        while i<numsLen:
            if nums[i] in dictRepeat:
                dictRepeat[nums[i]] += 1    
            else:
                dictRepeat[nums[i]] = 1
                if nums[i] >= 0:
                    numsP.append(nums[i])
                elif nums[i] < 0:
                    numsN.append(nums[i])
            i+=1
        if dictRepeat.get(0,0) > 2:
        	ansList.append([0,0,0])
        #numsP.sort()
        #numsN.sort()
        #++- 0+-
        i=0     
        while i<len(numsP):
            #4x2 - 8 = 0
            if dictRepeat[numsP[i]] > 1 and numsP[i] != 0:
                c = -2*numsP[i]
                if c in dictRepeat:
                    ansList.append([c,numsP[i],numsP[i]]) 
            k=i+1
            while k<len(numsP):
                c = - numsP[i] - numsP[k]
                if c in dictRepeat:
                    ansList.append([c,numsP[i],numsP[k]])
                k+=1
            i+=1  

        #+--
        i=0
        while i<len(numsN):   
            #-4x2 + 8 = 0
            if dictRepeat[numsN[i]] > 1:
                c = -2*numsN[i]
                if c in dictRepeat:
                    ansList.append([numsN[i],numsN[i],c]) 
            k=i+1
            while k<len(numsN):
                c = - numsN[i] - numsN[k]
                if c in dictRepeat:
                    ansList.append([numsN[i],numsN[k],c])
                k+=1

            i+=1  
        return ansList
        
            


def main():
    mycls = Solution()
    res = mycls.threeSum(nums=[-2,-1,0,2,-1,0,1,2,3,4])
    print("res=",res)

    import random
    testList=[]
    for xx in range(1,2000):
        alist=[]
        for x in range(1,random.randint(66,99)):
            alist += [random.randint(-500,500)] 
        testList.append(alist)

        #mycls = Solution()
        res = mycls.threeSum(nums=alist)
        print("alist=",alist,"res=",res)
    

if __name__ == '__main__':
    main()
