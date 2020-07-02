#38. 外观数列
#38. Count and Say

class Solution:
    def countAndSay(self, n: int) -> str:
        #输出字符串string1='1',从‘1’开始
        string1 = '1' 
        #首先先理解题，输入的整型数字都是上一个的读作的数，输入整型n，遍历（n-1），输出字符串
        for i in range(n - 1):            
            #首先将指针指向string1的第一项，赋值给a
            a = string1[0]
            #count用来计数，每一次循环都是从0开始计数
            count = 0  
            #形成新的字符串string2，在这个循环的末端将string2赋值给string1，最后输出i=n-1时string1的值
            string2 = ''
            #用b遍历string1的每一项
            for b in string1:
                #存在两种情况，第一种情况是a和string1[0]相等，count自加一，连续相等几次，count自加一几次
                if a == b:                    
                    count += 1 
                #不等时，连续中断， 形成新的字符串string2，相当于count个a，count转换成字符串可直接相加
                else:                    
                    string2 += str(count) + a
                    #将指针指向string1的新一项，赋值给a，内循环重新开始
                    a = b 
                    #count至少为1，所以从1开始，内循环重新开始
                    count = 1
            #当前的整数，遍历上一个字符串完了，形成新的字符串string2，相当于count个a，count转换成字符串可直接相加
            string2 += str(count) + a            
            string1 = string2 
        #输出字符串string1
        return string1
