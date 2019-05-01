
class Solution(object):
    
    def get_survives_num(self, n, k):
        #玩家从1开始到n编号，报数也从1开始到k，循环
        '''
        思路一：模拟这个过程，每次踢掉一个人后，将数组【A,k,B】切分为两部分【A】和【B】，交换位置变为【B,A】;直到数组长度为1
        '''
        players = list(range(1,n+1))
        while len(players)>1:
            '''
            n=6, [1,2,3,4,5,6] k=6时，k%n == 0应该去掉第六个元素，所以idx=len(players)-1
            '''
            eliminated_idx = len(players)-1 if k%len(players) == 0 else k%len(players)-1 
            #print("eliminated_idx=",eliminated_idx,players[eliminated_idx],"=",players)
            players = players[eliminated_idx+1:] + players[:eliminated_idx]
        return players[0]

#main-function  
def main():
    #input
    def scan():
        try:
            n, k = [int(e) for e in input().split()]
            return n, k
        except EOFError:
            return None
            
    mycls = Solution()
    _n_k = scan()
    while _n_k:
        res = mycls.get_survives_num(_n_k[0], _n_k[1])
        print(res)
        _n_k = scan()
        
      
if __name__ == '__main__':
    main()








