# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: 'TreeNode') -> 'int':
        def getMaxSum(node: 'TreeNode',maxNodeSum) :
            if not node: return [0,maxNodeSum]
            lsum, maxNodeSum = getMaxSum(node.left, maxNodeSum)
            rsum, maxNodeSum = getMaxSum(node.right, maxNodeSum)
            if node.val < 0:
                a_value = max(lsum,rsum)
                maxNodeSum = max(maxNodeSum, a_value)
                node.val += a_value
            else:
                node.val = max(node.val+lsum, node.val+rsum, node.val)
                maxNodeSum = max(maxNodeSum, node.val+lsum+rsum, node.val+lsum, node.val+rsum, node.val)
            return [node.val,maxNodeSum]
        maxNodeSum = root.val
        lsum, maxNodeSum = getMaxSum(root.left, maxNodeSum)
        rsum, maxNodeSum = getMaxSum(root.right, maxNodeSum)
        return max(maxNodeSum,lsum,rsum) if root.val < 0 else max(maxNodeSum,root.val+lsum,root.val+rsum,root.val+lsum+rsum,root.val)

if __name__ == '__main__':
    a=-1
    def tt(num):
        print('tt f()',a)
    tt(2)