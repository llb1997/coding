class Solution:
    def isAnagram(self,s,t) :
        if len(s) !=len(t) :#当s和t的长度不一样时，t 一定不是 s 的字母异位词，返回False
            return False
        set_s=set(s)   #获得不重复元素序列
        set_t=set(t)
        s=list(s)     #获得不重复元素列表
        t=list(t)
        if set_s==set_t :   #元素个数相等，不相等返回False
            for i in range(len(s)):
                if s.count(i) != t.count(i) :#遍历s和t中每一个元素的个数，只要有一个相同元素个数不相等，返回False
                    return False
            return True
        else:
            return False

if __name__=='__main__':  #必须有，表明该模块自身在运行
    print(Solution().isAnagram('aacg','aagc'))
    print(Solution().isAnagram('aacb','bbgc'))