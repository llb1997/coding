66. 加一

给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

示例 2:
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

解题过程：

在本地运行，需要在最后添加（if前面没有任何空格）
if __name__=='__main__':
    a=Solution()
    b=a.plusOne([1,1,1,9])
    c=a.plusOne([9])
    d=a.plusOne([9,9])
    e=a.plusOne([9,9,9])
    f=a.plusOne([1,1,1,1])
    print(b,c,d,e,f)