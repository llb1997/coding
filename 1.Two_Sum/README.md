
### 1. 两数之和

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。


示例:

        给定 nums = [2, 7, 11, 15], target = 9

        因为 nums[0] + nums[1] = 2 + 7 = 9

所以返回 [0, 1]


解题过程：

首先判断两种特殊情况，一种是nums数组为空，另一种nums中只有一个元素

a从0开始，b从1开始，

如果nums[a]不等于nums[b],则证明nums[b]不是重复项，将nums[b]赋值给nums[a+1],a，b

指针分别指向下一个（a自加一，b自加一）

否则，仅仅将指针移向b的下一个（b自加一）

在循环中将不重复项赋值给nums[a+1],所以返回移除后数组的新长度，返回的是a+1
