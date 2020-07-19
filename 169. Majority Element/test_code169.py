from collections import Counter
from code169 import Solution

p=Solution.majorityElement([3,2,3])
q=Solution.majorityElement([2,2,1,1,1,2,2])

def test1():
    assert 3 == p
def test2():
    assert 2 == q

if __name__ == "__main__":
    test1()
    test2()
        
