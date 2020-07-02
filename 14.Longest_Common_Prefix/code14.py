#最长公共前缀
#14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = lambda i:len(i))
        if len(strs) == 0:
            return ""
        if strs[0] == 0:
            return ""
        count = 0
        sum = ""
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if strs[0][i] == strs[j][i]:
                    count += 1
            if count == len(strs):
                sum += strs[0][i]
                count = 0
            else:
                break
        return sum
