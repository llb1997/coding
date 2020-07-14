class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def genTree(self, arr):
        def gen(arr, i):
            if i < len(arr):
                tn = TreeNode(arr[i]) if arr[i] is not None else None
                if tn is not None:
                    tn.left = gen(arr, 2 * i + 1)
                    tn.right = gen(arr, 2 * i + 2)
                return tn
        return gen(arr, 0)
    
    def isSymmetric(self, root):
        if not root: return True
        def bfs(root1, root2):
            if not root1 and not root2: return True
            if not root1 or not root2: return False
            if root1.val != root2.val: return False
            return bfs(root1.left, root2.right) and bfs(root1.right, root2.left)
        return bfs(root.left, root.right)


if __name__ == '__main__':
    root = Solution().genTree([1,2,2,None,3,None,3])
    print(Solution().isSymmetric(root))

