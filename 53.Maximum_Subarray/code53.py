#53. 最大子序和
#53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        elif len(nums)==1:
            return nums[0]
        elif max(nums)<=0:
            return max(nums)
            
        a=nums[0]
        max_=a
        for i in range(1,len(nums)):
            if a+nums[i]>nums[i]:
                max_=max(a+nums[i],max_)
                a+=nums[i]
            else:
                max_=max(nums[i],max_)
                a=nums[i]
        return max_
