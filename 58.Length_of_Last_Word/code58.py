#58. 最后一个单词的长度
#58. Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s==None :
            return 0
        else:
            #把首尾的空格去掉
            s=s.strip(' ')
            #以空格为分隔符，返回分割后的字符串列表
            x=s.split(' ')
            return len(x[-1])
