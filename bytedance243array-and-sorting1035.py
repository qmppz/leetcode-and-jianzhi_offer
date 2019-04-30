
class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        length = [1]
        i=1
        while i<len(nums):
            if nums[i] > nums[i-1]:
                length.append(length[i-1]+1)
            else:
                length.append(1)
            i+=1
        return max(length)

def main():
    mycls = Solution()
    res = mycls.findLengthOfLCIS(nums=[1,3,5,4,7])

    print(res)

if __name__ == '__main__':
    main()