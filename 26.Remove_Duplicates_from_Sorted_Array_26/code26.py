#删除排列数组中的重复项
#26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0|len(nums)==1:
            return len(nums)
        a,b=0,1
        while b<len(nums):
            if nums[a]!=nums[b]:
                nums[a+1]=nums[b]
                a+=1
                b+=1
            else:
                b+=1
        return a+1
