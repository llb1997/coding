#两数之和
#1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if i==j:
                    break
                if nums[i]+nums[j]==target:
                    return [i,j]
