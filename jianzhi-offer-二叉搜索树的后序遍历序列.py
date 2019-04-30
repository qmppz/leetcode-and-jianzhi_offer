'''
jianzhi-offer-二叉搜索树的后序遍历序列
https://www.nowcoder.com/practice/a861533d45854474ac791d90e447bafd?tpId=13&tqId=11176&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

参考解法：链接：https://www.nowcoder.com/questionTerminal/a861533d45854474ac791d90e447bafd
来源：牛客网

BST的后序序列的合法序列是，对于一个序列S，最后一个元素是x （也就是根），如果去掉最后一个元素的序列为T，那么T满足：T可以分成两段，前一段（左子树）小于x，后一段（右子树）大于x，且这两段（子树）都是合法的后序序列。完美的递归定义 : ) 。
'''


# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        #BST的后序序列的合法序列是，
        #对于一个序列S，最后一个元素是x （也就是根），
        #如果去掉最后一个元素的序列为T，那么T满足：T可以分成两段，前一段（左子树）小于x，后一段（右子树）大于x，且这两段（子树）都是合法的后序序列。完美的递归定义 : ) 。
        '''
        每次以最末尾的元素 m，分割序列，前部分小于m,后半部分大于m
        
        '''
        '''
        #返回小于 m 的数中 的最大角标
        def get_maxi(s,e,m,seq):
            i, j=s,e
            if s>e: return -1
            while i<j:
                mid=(i+j)//2
                if seq[mid]>m:
                    j=mid-1
                else:
                    #seq[mid]小于m，不会出现相等的情况
                    i=mid+1
            return i if seq[i]<m else: i-1
        def valid(s,e,seq):
            maxi = get_maxi(s,e,seq)
            if maxi-s   
        '''
        '''
        方法二：从后往前，对序列的每一个值 end_val，都进行如下判断：
            一定能将序列分为两部分，前部分都小于end_val，后部分都大于end_val；都满足则继续往前更新end_val的值
            若不满足则False
        def valid(sequence,s,e):
            if s>=e:return True
            end_val = sequence[e]
            new_e = e-1
            new_s = s
            while sequence[s]<end_val:
                s+=1
            mid = s
            while sequence[s]>end_val:
                s+=1
            if s!=e:return False
            else:
                if new_s == mid-1
                return valid(sequence,new_s,mid-1) and valid(sequence,mid,new_e)
        res = valid(sequence,0,len(sequence)-1)
        
        return 'Yes' if res else 'No'
        TMD不是返回 yes no 是返回true false，shadiaotimu
        '''
        if len(sequence)<3:return True if len(sequence)>0 else False
        
        i=len(sequence)-1
        while i>=0:
            k=0
            while k<i:
                if sequence[k]<sequence[i]:
                    k+=1
                else:break
            
            while k<i:
                if sequence[k]>sequence[i]:
                    k+=1
                else:break
            if k!=i: return False
            i-=1
        return True
        
        
            
            
            
            
            
            
            
            
            
        
        
        
        
        
        
        
        

        
        
        
        