#搜索插入位置
#35. Search Insert Position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            if (target<nums[0]):
                return 0
            elif (target>nums[len(nums)-1]):
                nums.append(target)
                return len(nums)-1
            else:
                for i in range (0,len(nums)):
                    if nums[i]<target and nums[i+1]>target:
                        nums.insert(i+1, target)
                        return i+1

#折半查找

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <=right:
            mid = (right +left) // 2 
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


