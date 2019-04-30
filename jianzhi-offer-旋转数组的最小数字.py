'''
jianzhi-offer 旋转数组的最小数字
https://www.nowcoder.com/practice/9f3231a991af4f55b95579b44b7a01ba?tpId=13&tqId=11159&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

'''

# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code h`ere
        '''
        方法一： 递归 maximum recursion depth exceeded
        '''
        '''
        if len(rotateArray)==0 :return 0
        def getminnum(i, j):
            if i==j: 
                return rotateArray[i]
            mid = (i+j)//2
            if rotateArray[i]>=rotateArray[mid]:
                return getminnum(i+1,mid)
            else:
                #rotateArray[mid]>=rotateArray[j]:
                return getminnum(mid+1,j)
            
        return getminnum(0, len(rotateArray)-1)
        '''
        #---------------------------------------
        '''
        方法二：顺序
        样例：[1,1,1,1,1,0,1]
        '''
        if len(rotateArray)==0 :return 0
        
        i, j = 0, len(rotateArray)-1
        
        waitlist=[]
        while i<j:
            mid = (i+j)//2
            if rotateArray[i] > rotateArray[mid]:
                i+=1
                j=mid
            elif rotateArray[mid] > rotateArray[j]:
                i=mid+1
            elif rotateArray[i] == rotateArray[mid] and rotateArray[j] == rotateArray[mid]:
                #缩小范围
                i+=1
                j-=1
            else: break
        return min(rotateArray[i],rotateArray[j])
                
                

        
        
        