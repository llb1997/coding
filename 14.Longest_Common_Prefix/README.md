14. 最长公共前缀

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:

所有输入只包含小写字母 a-z 。

解题过程：

求最长公共前缀，可以用最短的那一项去和其他项去比较，用 strs.sort(），默认是升序

首先，排除一些特殊项，比如strs="“或者strs[0]=”",返回""

外循环 i 遍历strs[0]返回索引值：

内循环 j 遍历strs返回索引值

count=0

一个字母一个字母进行比较，若相同则count+1,当一个字母比较完后，跳出内循环，若count等于strs的长度，则表明这个字母是所有元素的前缀，将count=0（重置为零）我们就开始比较下一个字母，直到count不等于strs的长度，跳出外循环我们return先前比较过的所有字母即可。

