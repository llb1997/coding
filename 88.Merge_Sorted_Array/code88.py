#合并两个有序数组
#88. Merge Sorted Array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[0:m+n] = sorted(nums2 + nums1[0:m])
        return nums1
