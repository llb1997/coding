# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def genTree(self, arr):
        def gen(arr, i):
            if i < len(arr):
                tn = TreeNode(arr[i]) if arr[i] is not None else None
                if tn is not None:
                    tn.left = gen(arr, 2 * i + 1)
                    tn.right = gen(arr, 2 * i + 2)
                return tn
        return gen(arr, 0)
        
    def maxDepth(self, root):
        if root is None:
            return 0

        q = [(1, root)]

        
        while q:
            mount, node = q.pop(0)
            if node.left:
                q.append((mount+1,node.left))
            if node.right:
                q.append((mount+1,node.right))
        return mount



if __name__ == '__main__':
    root = Solution().genTree([3,9,20,None,None,15,7])
    print(Solution().maxDepth(root))
    
    root = Solution().genTree([3,9,20,None,None])
    print(Solution().maxDepth(root))
    