class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        #p和q都是None
        if p==None and q==None:
            return True
        #p和q至少一个是None    
        if p==None or q==None:
            return False
        #值不相同，返回否
        if p.val !=q.val :
            
            return False

        #左右都出发，看两个是否一样，出现一个返回False，每一处都相同，则返回 True
        return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)

