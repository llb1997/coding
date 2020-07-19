from collections import Counter

class Solution:
    def majorityElement(nums):
        if not nums:
            return False
        else:
            m=Counter(nums).most_common(1)
            if m[0][1]>(len(nums)/2):
                return m[0][0]
            else :
                return False

p=Solution.majorityElement([3,2,3])
q=Solution.majorityElement([2,2,1,1,1,2,2])

def test1():
    assert 3 == p
def test2():
    assert 2 == q

if __name__ == "__main__":
    test1()
    test2()
        
