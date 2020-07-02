#整数取反
#7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        a=0
        if x>=0:
            while x>0:
                a=a*10+x%10
                x//=10
        else:
            x=-x
            while x>0:
                a=a*10+x%10
                x//=10
            a=-a
        if a<-2**31 or a>2**31-1:
            return 0
        else:
            return a
