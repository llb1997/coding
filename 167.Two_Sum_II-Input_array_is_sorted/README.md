167. 两数之和 II - 输入有序数组


给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:
返回的下标值（index1 和 index2）不是从零开始的。

你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

示例:
输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

解题过程：

将 j 定义为numbers最后一个索引值， i 从零开始遍历，根据题目可知 i < j ,用while循环，当循环条件为False时，跳出循环，

因为是按顺序排列的数组，i 从前开始遍历，j 从后开始遍历，

当numbers[i] + numbers[j] > target 时 j 左移（自减一），

当numbers[i] + numbers[j] < target 时 i 右移（自加一），最后一种情况返回[i+1,j+1]