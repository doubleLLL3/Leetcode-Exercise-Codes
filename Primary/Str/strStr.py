def strStr(haystack, needle):
        '''
        1.先判断特殊needle为空的情况以及hay长度小于need的情况
        2.用两个指针分别指向两个字符串，前者一直往下遍历，后者如果匹配不上就重置为0
        3.直到匹配完后者或者遍历完前者为止(关键点：如何提取index)
        '''
        # if needle == '':
        #     return 0
        # if len(haystack) < len(needle):
        #     return -1
        # h = 0
        # n = 0
        # index = -1
        # while n < len(needle):
        #     if h == len(haystack):
        #         index = -1
        #         break
        #     if haystack[h] == needle[n]:
        #         index = h
        #         h += 1
        #         n += 1
        #     else:
        #         if h == len(haystack):
        #             break
        #         h = h - n + 1
        #         n = 0
        #         index = -1
        # return index - len(needle) + 1 if index != -1 else -1

        '''
        使用KMP算法！
        1.首先计算出模式串的PMT表--部分匹配表
        2.遍历要匹配的主串
        '''
        if needle == '':
            return 0
        # PMT
        next = []
        next.append(-1)
        i, j = 0, -1
        while i < len(needle):
            if j == -1 or needle[i] == needle[j]:
                i += 1
                j += 1
                next.append(j)
            else:
                j = next[j]

        # KMP
        j = 0
        i = 0
        while i < len(haystack):
            if j == -1 or haystack[i] == needle[j]:
                if j == len(needle)-1:
                    return i - len(needle) + 1
                i += 1
                j += 1
            else:
                j = next[j]
        return -1




print(strStr("", ""))
print(strStr("hello", "ll"))
print(strStr("ababababca", "abababca"))
print(strStr("mississippi", "issipi"))
print(strStr("aaa", "aaaaa"))