from code1137 import Solution
a=Solution().tribonacci(25)
b=Solution().tribonacci(4)

def test1():
    assert a == 1389537 
def test2():
    assert 4 == b

if __name__ == '__main__': 
    test1()
    test2()
