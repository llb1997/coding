from collections import Counter

class Solution:
    def majorityElement(nums):
        if not nums: 
            return False
        else:
            m=Counter(nums).most_common(1)#返回次数最多的一个[[元素，次数]]列表
            if m[0][1]>(len(nums)/2):   #如果该元素次数大于(n/2),返回次数，否则返回False
                return m[0][0]
            else :
                return False


if __name__ == "__main__":

    p=Solution.majorityElement([3,2,3])
    q=Solution.majorityElement([2,2,1,1,1,2,2])

    print(p)
    print(q)
