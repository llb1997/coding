
from code242 import Solution

a=Solution().isAnagram('aacg','aagc')
b=Solution().isAnagram('aacb','bbgc')

def test1():
    assert True == a
def test2():
    assert False == b
if __name__ == '__main__': 
    test1()
    test2()