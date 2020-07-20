#Definition for a binary tree node.
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def genTree(self,arr):#该函数将列表生成二叉树
        def gen(arr, i):
            if i < len(arr):
                tn = TreeNode(arr[i]) if arr[i] is not None else None
                if tn is not None:
                    tn.left = gen(arr, 2 * i + 1)
                    tn.right = gen(arr, 2 * i + 2)
                return tn
        return gen(arr, 0)

    #类似斐波那契f(n)=f(n-1)+f(n-2)+1
    # height(p)--->   −1                                      p为空
    #          --->   1+max(height(p.left),height(p.right))​   其他​

    #isBalanced(root) ---->isBalanced(root.left) and isBalanced(root.right)将跟分成左节点和右节点
    #类似  isBalanced(n)   ---->  isBalanced(n-1)

    def isBalanced(self,root):
        if not root :
            return True

        #判断条件a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
        
        if abs(self.height(root.left)-self.height(root.right))>1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self,root):
        if not root: return 0
        return max(self.height(root.left), self.height(root.right)) + 1

if __name__ == '__main__':
    root1 = Solution().genTree([3,9,20,None,None,15,7])
    root2 = Solution().genTree([1,2,2,3,3,None,None,4,4])
    print(Solution().isBalanced(root1))
    print(Solution().isBalanced(root2))