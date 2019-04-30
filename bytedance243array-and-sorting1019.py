class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = sorted(list(set(nums)))
        # if len(nums) < 2: return len(nums) 
        # lastNum = nums[0]; ans = 1 ; maxlen = 1
        # for e in nums[1:]:
        #     if e == lastNum+1: maxlen += 1
        #     elif e != lastNum: ans = max(ans, maxlen) ; maxlen = 1
        #     lastNum = e
        # return max(ans, maxlen)

        if len(nums) < 2:
            return len(nums)
        LC = []
        for item in set(nums):
            #head small
            idxHead, idxTail = -1,-1
            i=0
            while i<len(LC):
                if len(LC[i]) == 0:  i+=1;  continue
                if idxHead == -1 and item+1 in LC[i]: 
                    idxHead = i
                    LC[i].add(item)
                if idxTail == -1 and item-1 in LC[i]:  
                    idxTail = i
                    LC[i].add(item)
                i+=1
            if idxHead + idxTail == -2:
                #not find
                s = set()
                s.add(item)
                LC.append(s)
            elif idxHead >= 0 and idxTail >= 0:
                LC[idxTail] = LC[idxTail] | LC[idxHead]
                LC[idxHead] = set()
        return max([len(sq) for sq in LC])

def main():
    mycls = Solution()
    res = mycls.longestConsecutive(nums=[1,2,0,1])
    print(res)

if __name__ == '__main__':
    main() 
