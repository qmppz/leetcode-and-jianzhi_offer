'''
https://leetcode-cn.com/problems/longest-palindromic-substring/
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #方法一
        '''
        if len(s) == 0 : return ''
        elif len(s) == 1: return s
        elif len(s) == 2: return s if s[0] == s[1] else s[0]
        resStr = ''
        i=0
        while i < len(s)-1:
            if i+2 <len(s) and s[i] == s[i+2]:
                tmpStr = s[i]+s[i+1]+s[i+2]
                center, increment = i+1, 1+1
                i_incre = center+increment
                j_incre = center-increment
                while i_incre<len(s) and j_incre>=0:
                    if s[i_incre] == s[j_incre]:
                        tmpStr = s[i_incre] + tmpStr + s[i_incre]
                        increment += 1
                        i_incre = center+increment
                        j_incre = center-increment
                    else: break
                resStr = tmpStr if len(tmpStr) > len(resStr) else resStr
            if s[i] == s[i+1]:
                tmpStr = s[i]+s[i+1]
                center, increment = i+0.5, 0.5+1
                i_incre = int(center+increment)
                j_incre = int(center-increment)
                while i_incre<len(s) and j_incre>=0:
                    if s[i_incre] == s[j_incre]:
                        tmpStr = s[i_incre] + tmpStr + s[i_incre]
                        increment += 1
                        i_incre = int(center+increment)
                        j_incre = int(center-increment)
                    else: break
                resStr = tmpStr if len(tmpStr) > len(resStr) else resStr
            i += 1
        return resStr if len(resStr)>0 else s[0]
        '''
        '''
        方法二
        时间复杂度 O(N^2)
        思路：中间开花法，遍历str每一个字符，对于每一个点，判断左右两侧字符是否相同，直到不同为止，记录下长度，坐标
        对于每一个点，回文字符有两种情况，noon 和 non
        '''
        '''
        maxLenStr=''
        for i in range(len(s)):
            
            #noon
            l=i
            r=i+1
            while l>=0 and r<=len(s)-1:
                if s[l]==s[r]: l-=1;r+=1
                else: tmpStr = s[l+1:r];maxLenStr = tmpStr if r-l-1 > len(maxLenStr) else maxLenStr;break
            if l<0 or r>len(s)-1:tmpStr = s[l+1:r];maxLenStr = tmpStr if r-l-1 > len(maxLenStr) else maxLenStr    

            #non
            l=i-1
            r=i+1
            while l>=0 and r<=len(s)-1:
                if s[l]==s[r]: l-=1;r+=1
                else: tmpStr = s[l+1:r];maxLenStr = tmpStr if r-l-1 > len(maxLenStr) else maxLenStr;break
            if l<0 or r>len(s)-1:tmpStr = s[l+1:r];maxLenStr = tmpStr if r-l-1 > len(maxLenStr) else maxLenStr


        return maxLenStr
        '''
        
        '''
        方法三：Manacher法
        T=O(N)
        
        '''
            
            
            
        
        
        