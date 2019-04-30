'''
jianzhi-offer-栈的压入、弹出序列
https://www.nowcoder.com/practice/d77d11405cc7470d82554cb392585106?tpId=13&tqId=11174&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''

# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        '''
        1 2 3 4 5 push
        1 3 2 4 5 pop
        错误的思路一：
        使用s , e表示在pushV中需要进行比对的开始结束位置，初始s=e=0
        
        k从0到len(popV)遍历popV，对于每一个popV[k],
        idx_in_push = pushV.find( popV[k] )
        
        然后逐一比对 pushV[e:s+1:-1]（push逆序） 与  popV[k:k+e-s+1]
        有一个错则失败return False，否则继续递增k，
        '''
        '''
        if len(pushV) == len(popV) and len(pushV)<=1:return True
        if not pushV or not popV: return False
        
        s = e = 0
        k = 0
        while k<len(popV):#for  k in range(len(popV)):
            idx_in_push = -1
            #查找 idx
            for idx,elem in enumerate(pushV[s:]):
                if elem == popV[k]:
                    idx_in_push=s+idx
                    break
            if idx_in_push == -1: return False
            
            e = idx_in_push
            
            tmp_i = e-1# 在s e之间遍历的角标 tmp_i
            k_add = k+1 #与之对应的 k_add
            # 然后逐一比对 pushV[e:s+1:-1]（逆序遍历） 与  popV[k:k+e-s+1]
            while tmp_i>=s:
                if pushV[tmp_i] == popV[k_add]:
                    tmp_i-=1
                    k_add+=1
                else: return False
            s=e=idx_in_push+1
            
            k = k_add
        return True
        '''
        
        '''
        将
        方法二：对pushV序列模仿入栈过程，然后出栈与popV一一比对
        定义角标k，遍历popV, 对于每一个 popV[k]，先与stack的top值比较，
                    若不等则再逐个与pushV[s:]的值比较,不等于则pushV[s]入栈
                                                   相等则出栈
                    若相等则stack top 出栈
                    
        '''
        if len(pushV) == len(popV) and len(pushV)<1:return True
        if not pushV or not popV: return False
        
        #push 第一个元素入栈
        stack = [pushV[0]]
        #push的遍历 开始角标，从0开始
        s=1
        idx_in_push=-1
        k=0
        while k<len(popV):
            #与栈顶比较
            if popV[k] == stack[-1]:
                #stack pop
                stack.pop(-1)
            else:
                #flag: 是否在push中找到 popV[k]
                find_in_push = -1
                for i,v in enumerate(pushV[s:]):
                    if popV[k] == v:
                        s = s+i+1
                        find_in_push = 1
                        break
                    else:
                        stack.append(v)
                if find_in_push == -1: return False
            k+=1
        return True
                
            
            
            
            
        
        
        
        