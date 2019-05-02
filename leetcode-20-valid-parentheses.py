'''
leetcode-20-valid-parentheses.py
有效的括号
https://leetcode-cn.com/problems/valid-parentheses/

#
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        思路一：
        栈的思想，循环遍历s，判断是否是 右括号，是，则判断与当前栈顶括号能配对，能则弹出不入栈，不能则报错；
        
        若是左括号，是则入栈
        最后栈不为空，报错
        '''
        if not s:return True
        stack = [s[0]]
        #for语句中，对s切片则相当于重新用一块内存保存切片后的值，for内部的修改无法同步修改
        #for kh in s[1:]:
        s=s[1:]
        for kh in s:
            if kh == '(' or kh == '[' or kh == '{':
                stack.append(kh)
            elif (len(stack)>0) and((stack[-1] == '(' and kh == ')') or (stack[-1] == '[' and kh == ']') or (stack[-1] == '{' and kh == '}')):
                stack.pop()
            else: return False
        return True if len(stack)==0 else False
        '''
        细节
        #多个元组
        if (False,False,False,False,False,False,False) :
        print("#元组 true,这里判断的只是元组是否为空，并不关心元组的元素是true还是false")
        #元组 true,这里判断的只是元组是否为空，并不关心元组的元素是true还是false

        #单个true 或 false在括号中，python将其解析为 bool型
        '''