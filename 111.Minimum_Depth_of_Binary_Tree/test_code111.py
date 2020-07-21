from code111 import Solution
def test1():
    root1 = Solution().genTree([3,9,20,None,None,15,7])

    a=Solution().minDepth(root1)


    assert 2 == a

if __name__ == '__main__': 
    test1()
    