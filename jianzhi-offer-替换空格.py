'''
jianzhi-offer 替换空格
https://www.nowcoder.com/practice/4060ac7e3e404ad1a894ef3e17650423?tpId=13&tqId=11155&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking

题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        '''
        方法一：按空格分割成多个数组，然后对这些数组间加上 %20 再重新连接
        简单题
        注意：
        split()会在有空格的地方分割数组，将这个位置以及其相连的位置上的一串空格全部去掉作为一个分割点
        split(' ') 指定了空格字符，则遇到一个空格字符' '就分割一次，连续空格的情况就会分割出很多长度为0的数组
        '''
        #每一次分割必定少一个且仅少一个 空格
        return '%20'.join(s.split(' '))