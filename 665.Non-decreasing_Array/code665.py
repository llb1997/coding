#665. 非递减数列
#665. Non-decreasing Array

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        m = 0
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                m += 1
                if i+1 < len(nums) and i-2 >= 0:
                    if nums[i-1] > nums[i+1] and nums[i-2] > nums[i]:
                        return False
            if m > 1:
                return False
        return True
