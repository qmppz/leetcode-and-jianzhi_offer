import sys
class Solution:
    def get_dot_num(self, nums):
        a=-1
        alist=[-1,-2,-3]
        b = alist.copy()
        def ff(aa,aalist):
            aa=aa*a
            aalist = aalist+alist
            return aa,aalist
        
        return ff(99,[9,99,999])

if __name__ == '__main__':
    
    N = int(input().split()[0])
#
    #print(_nums)
    cls =  Solution()
    res = cls.get_dot_num(N)
    print(res)
    
    
    '''
    4
    1 2 1 3
    1 2 1 5
    1 2 1 9
    4 4 4 6
    
    4
    1 1 3 1
    2 1 5 1
    2 1 9 1
    4 4 7 4
    
    
    '''
        