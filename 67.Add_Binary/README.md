67. 二进制求和

给你两个二进制字符串，返回它们的和（用二进制表示）。
输入为 非空 字符串且只包含数字 1 和 0。
 
示例 1:
输入: a = "11", b = "1"
输出: "100"

示例 2:
输入: a = "1010", b = "1011"
输出: "10101"
 
提示：
每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。

在本地运行

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #二进制转十进制
        a=int(a,2)
        b=int(b,2)
        y=a+b
        #建立模块，调用模块
        def mybin(x):
            return bin(x).replace('0b', '')
        return mybin(y)
if __name__=='__main__':
    a=Solution()
    b=a.addBinary('111','110')
    c=a.addBinary('101','000')
    d=a.addBinary('110','101')
    print(b,c,d)
