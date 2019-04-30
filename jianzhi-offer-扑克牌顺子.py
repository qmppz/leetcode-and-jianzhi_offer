'''
jianzhi-offer-扑克牌顺子
https://www.nowcoder.com/practice/762836f4d43d43ca9deb273b3de8e1f4?tpId=13&tqId=11198&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


题目描述
LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。
'''

# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        '''
        numbers：list[int:5]
        思路一：先排序，记录王的个数，然后从除去王后最小的牌开始，看看每次加一后的牌是否存在
        ps:list没有find方法，index方法找不到会报错
        '''
        if numbers == [] : return  False
        numbers.sort()
        wang_cnt = numbers.count(0)
        for i in range(wang_cnt,4):
            if numbers[i+1] - numbers[i] == 0:
                return False
            elif numbers[i+1] - numbers[i] > 1:
                wang_cnt -= numbers[i+1] - numbers[i] - 1
                if wang_cnt<0:return False
        return True