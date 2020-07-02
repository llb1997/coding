#20. 有效的括号
#20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        #第一种情况s为空时，被认为是有效字符，返回True
        if s==None:
            return True
        #第二种情况s长度为奇数时，不是有效字符，返回False
        elif len(s)%2!=0:
            return False   
        #还有其他情况
        else:
            d={'(':')','[':']','{':'}'}
            #建立一个stack=[]，进行初始化
            stack=[]
            #遍历s中的所有元素
            for i in s:
                #第一种情况stack=[]或者i在d中，需要将i添加到stack末尾
                if i in d or  stack==[]:
                    stack.append(i)
                #第二种情况stack的最后一个元素在d中，同时stack的最后一个元素对应的值和i相等，将stack的最后一个元素删除
                elif stack[-1] in d and d[stack[-1]] == i:
                        stack.pop()
                #其他情况返回False
                else:
                        return False
            #最后stack==[]，stack为空返回True，否则返回False
            return  stack==[]
