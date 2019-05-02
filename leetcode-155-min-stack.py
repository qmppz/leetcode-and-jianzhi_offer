'''
leetcode-155-min-stack.py
最小栈
https://leetcode-cn.com/problems/min-stack/

#
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
'''


'''
【关键是 在当前最小值弹出栈的时候如何在O(1)的时间复杂度中找到下一个最小值】
普通解法：使用两个栈
参考解法：使用一个栈；两次pop push法 和 记录差值法
https://www.cnblogs.com/lightwindy/p/8512214.html

#两次pop push法：每次push时，如果出现比当前最小值还小的数，那么 push两次，分别把当前最小值和新的最小值放入栈中；这样操作的含义就是 相邻的位置保存了当前这个最小值和次小值，以便于最小值被pop的时候，能够欧迅速找到次小值； 空间可能会超过O(N)

#记录差值法：空间更省，只用O(N)的栈
https://www.cnblogs.com/lightwindy/p/8512214.html
self.min = oxFFFFFFFF #数值
self.stack = [] # 与某个阶段的最小值的差值
就是用差值来寻找当前最小值与次小值

'''
#记录差值法:空间更省
#https://www.cnblogs.com/lightwindy/p/8512214.html

class MinStack(object):
 
    def __init__(self):
        self.min = 0xFFFFFFFF #数值
        self.stack = [] # 与某个阶段的最小值的差值
 
    def push(self, x): 
        if not self.stack:
            self.min = x
        #保存与当前最小值的差值
        self.stack.append(x - self.min)
        if x < self.min:
            self.min = x
 
    def pop(self):
        #正常pop
        peak = self.stack.pop()
       #差值小于0，则代表当时入栈的时候，这个差值对应的数 比 当时遇到的最小值还小，所以这里需要更新最小值，也就是恢复对应这个数
        if peak < 0:
            self.min = self.min - peak
 
    def top(self):
        if self.stack[-1] < 0:
            return self.min
        else:
            return self.min + self.stack[-1]
 
    def getMin(self):
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#-----------------------------------------------------------------------

#两次pop push法
'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        self.min_value = 0xFFFFFFFF
        
    def push(self, x: int) -> None:
        if len(self.min_stack) == 0 :
            self.min_stack.append(x)
            self.min_value = x
        else:
            #每次push时，如果出现比当前最小值还小的数，那么 push两次，分别把当前最小值和新的最小值放入栈中；先放旧的最小值，再放新的最小值；比如[3,4,1,2]依次入栈得到[3,4,3,1,2],3会重复
            if x <= self.min_value: #//此处必须为<=,否则可以试一下{0，1，0}的情况
                #先放旧的最小值
                self.min_stack.append(self.min_value)
                self.min_value = x
            #再放新的最小值
            self.min_stack.append(x)
            
    def pop(self) -> None:
        if len(self.min_stack) == 0 :
            return ;
        #当弹出的元素是当前最小值时，需要弹出两个数，第二个弹出的数就是次小值；比如[3,4,1,2]依次入栈得到[3,4,3,1,2]，所以弹出的时候需要两次
        pop_value = self.min_stack.pop()
        if pop_value == self.min_value:
            #且栈中还有元素
            if len(self.min_stack) > 0 :
                self.min_value = self.min_stack.pop()
            else:
                #栈已经为空，初始化最小值,（无意义操作，因为栈空时push会直接覆盖最小值
                self.min_value = 0xFFFFFFFF
        return pop_value
        
    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return self.min_value


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
'''