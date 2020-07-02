#两数之和 II - 输入有序数组
#167. Two Sum II - Input array is sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j=len(numbers)-1
        for i in range(len(numbers)):
            while i<j:
                if numbers[i]+numbers[j]==target :
                    return [i+1,j+1]
                elif numbers[i] + numbers[j] > target:
                    j -= 1
                else:
                    i += 1
