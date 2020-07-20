from code110 import Solution

root1 = Solution().genTree([3,9,20,None,None,15,7])
root2 = Solution().genTree([1,2,2,3,3,None,None,4,4])

a=Solution().isBalanced(root1)
b=Solution().isBalanced(root2)



def test1():
    assert True == a
def test2():
    assert False == b
if __name__ == '__main__': 
    test1()
    test2()