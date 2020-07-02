28. 实现 strStr()

实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串

出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2

示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

解题过程：

从三个方面来说
1）当 needle 是空字符串时，返回 0
2）needle 不在 haystack中，返回-1
3）str.find(sub)判断sub在不在str中，如果包含子字符串返回索引值的起始位置，否则返回-1
    return haystack.index(needle)

str.index(sub)判断sub在不在str中，如果包含子字符串返回索引值的起始位置，否则抛出异常
