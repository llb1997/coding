#66. 加一
#66. Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #有两种情况，第一种，末尾不是9，最后一项直接加一，（digits[-1]+=1）返回digits
        if 0<=digits[-1]<9:
            digits[-1]+=1
            return digits
        #第二种情况，末尾是9
        else:
            #遍历digits，从后往前
            for i in range(len(digits)-1,-1,-1):
                #出现第一个不为9的数直接加一，循环结束，不再和9比较，返回digits
                if digits[i]!=9:
                    digits[i]+=1
                    return digits
                #将i和i后面的所有都为0
                j=i
                while j<=len(digits)-1:
                    digits[j] = 0
                    j+=1
            #当出现9，99，999等等这种情况时
            digits[0] = 1
            digits.append(0)
        return digits
