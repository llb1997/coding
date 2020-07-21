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
    
    def minDepth(self, root):
        if not root :
            return 0
        if not root.left and not root.right:
            return 1

        #遍历root的左节点和右节点，
        # 再遍历root.left的左节点和右节点, 再遍历root.right的左节点和右节点
        # 找出min(当前最小值和根左节点的左右节点)(根右节点的左右节点)
        Tree_Node=[root.left,root.right]
        #float("inf"), float("-inf") 
        #正无穷，负无穷 
        min_Depth=float("inf")
        
        for i in Tree_Node:   
            if i :      
                min_Depth=min(self.minDepth(i),min_Depth)
    
        return min_Depth+1

if __name__ == '__main__':
    root1 = Solution().genTree([3,9,20,None,None,15,7])
    
    print(Solution().minDepth(root1))
   