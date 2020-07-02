#67. 二进制求和
#67. Add Binary

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
