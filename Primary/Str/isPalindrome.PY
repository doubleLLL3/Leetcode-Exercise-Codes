def isPalindrome(s):
        '''
        1.双指针对应遍历，遇到字母和数字才进行识别，并且不考虑字母大小写
        '''        
        # i = 0
        # j = len(s) - 1
        # while i < j:
        #     if not s[i].isalnum():
        #         i += 1
        #         continue
        #     if not s[j].isalnum():
        #         j -= 1
        #         continue
        #     if s[i].lower() == s[j].lower():
        #         i += 1
        #         j -= 1
        #         continue
        #     return False
        # return True

        '''
        使用filter过滤后，在反转比较即可
        '''
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))