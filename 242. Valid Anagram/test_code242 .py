def isAnagram(s,t) :
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


a=isAnagram('aacg','aagc')
b=isAnagram('aacb','bbgc')

def test1():
    assert True == a
def test2():
    assert False == b
if __name__ == '__main__': 
    test1()
    test2()