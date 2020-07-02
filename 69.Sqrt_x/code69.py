#69. x 的平方根
#69. Sqrt(x)

class Solution:
    def mySqrt(self, x: int) -> int:
        import math
        if x>=0:
            x=math.floor(math.sqrt(x))
            return x
