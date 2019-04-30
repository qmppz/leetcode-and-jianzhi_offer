
class Solution:

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums)==k: return min(nums)
        elif k==1: return max(nums)
        kL = [v for v in nums[:k]]
        i=k
        while i < len(nums):
            minNumIdx,minNum = 0, kL[0]
            for idx,v in enumerate(kL[1:]):
                if v < minNum:  minNumIdx = idx+1; minNum = v
            if nums[i] >= kL[minNumIdx]:
                kL[minNumIdx] = nums[i]
            i+=1
        return min(kL)

    def findKthLargest_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #return sorted(nums)[-k] #50ms fastest
        if len(nums) == 1:
            return nums[0]
        import random
        def partion(l,h):
            ri = random.randint(l,h)
            nums[l],nums[ri] = nums[ri],nums[l]
            pvt = nums[l]
            while l<h:
                while l<h and nums[h]>=pvt: h-=1
                nums[l] = nums[h]
                while l<h and nums[l]<=pvt: l+=1
                nums[h] = nums[l]
            nums[l] = pvt
            return l

        l,h=0,len(nums)-1
        pvtIdx = partion(l,h)
        while True:
            if pvtIdx == len(nums)-k:
                return nums[pvtIdx]
            if pvtIdx > len(nums)-k:
                pvtIdx = partion(l,pvtIdx-1)
            else:
                pvtIdx = partion(pvtIdx+1,h)



def main():
    mycls = Solution()
    res = mycls.findKthLargest(nums=[3,2,3,2,2,4,5,5,6],k=4)

    print(res)

if __name__ == '__main__':
    main()
 