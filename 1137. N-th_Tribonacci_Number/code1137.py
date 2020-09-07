class Solution:
    def tribonacci(self,n):
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        else:
            x=0
            y=z=1
            for i in range(n-2):
                x,y,z=y,z,x+y+z
            print(z)
            return z

if __name__ == '__main__': 
    Solution().tribonacci(25)
