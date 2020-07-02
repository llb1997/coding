#28. 实现 strStr()
#28. Implement strStr()

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle==None:
            return 0
        elif needle not in haystack:
            return -1
        else:

            return haystack.find(needle)
