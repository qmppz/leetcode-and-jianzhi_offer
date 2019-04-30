class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        nums1 =sorted(nums1 + nums2)
        return nums1[len(nums1)//2] if len(nums1)%2==1 else (nums1[len(nums1)//2] + nums1[len(nums1)//2-1])/2







if __name__ == '__main__':
	num = [-4,-3,-2,-1,0,1,2,3,4]
	for x in range(100,105):
		a = x
		print(a,~a)