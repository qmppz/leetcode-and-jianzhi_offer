class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #baseline
        return self.rotatedSearch(0,len(nums)-1,nums,target)

    def rotatedSearch(self,s,e,nums,target):
        
        if s>=len(nums) or e<0 or s>e:
            return -1
        l,h=s,e
        m = (s+e)//2
        if nums[m] == target:
            return m
        if nums[s] > nums[m]:
            # fanchang
            if target>nums[m] and target<=nums[e]: 
                #zhangchang erfen
                l,h=m+1,e
            else:
                return self.rotatedSearch(s,m-1,nums,target)
        elif nums[m] > nums[e]:
            #fanchang
            if target>=nums[s] and target<nums[m]:
                #zhengchang erfen
                l,h=s,m-1
            else:
                return self.rotatedSearch(m+1,e,nums,target)
        #meiyou fanchang
        while l<=h:
            mm = (l+h)//2
            if nums[mm] == target:
                return mm
            if nums[mm] > target:
                h=mm-1
            else:
                l=mm+1
        return -1

def main():
    mycls = Solution()
    res = mycls.search(nums=[3,4,5,6,1,2],target=2)

    print(res)

if __name__ == '__main__':
    main()