class Solution:
    def isAnagram(self,s,t) :
        if len(s) !=len(t) :
            return False
        set_s=set(s)
        set_t=set(t)
        s=list(s)
        t=list(t)
        if set_s==set_t :
            for i in range(len(s)):
                if s.count(i) != t.count(i) :
                    return False
            return True
        else:
            return False

if __name__=='__main__':
    print(Solution().isAnagram('aacg','aagc'))
    print(Solution().isAnagram('aacb','bbgc'))