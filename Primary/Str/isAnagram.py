def isAnagram(s, t):
        '''
        1.先使用长度作为第一条件筛选
        2.用两个字典存储字符和出现次数
        3.判断两个字典是否相同
        '''
        # if len(s) != len(t):
        #     return False
        
        # dict_s = {}
        # dict_t = {}
        # for i in range(len(s)):
        #     dict_s[s[i]] = dict_s.get(s[i], 0) + 1
        #     dict_t[t[i]] = dict_t.get(t[i], 0) + 1
            
        # if dict_s == dict_t:
        #     return True
        # return False

        '''
        排序后比较是否相等：

        '''
        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)
        '''
        放入字典时，一个加一个减，则只需要一个字典
        '''
        # if len(s) != len(t):
        #     return False
        # dict = {}
        # for i in range(len(s)):
        #     dict[s[i]] = dict.get(s[i], 0) + 1
        #     dict[t[i]] = dict.get(t[i], 0) - 1
        # for i in dict.values():
        #     if i != 0:
        #         return False
        # return True
        '''
        先遍历完一个字符串放入一个字典，再用另一个字符串来减，如果小于0则直接返回False
        '''
        # if len(s) != len(t):
        #     return False
        # dict = {}
        # for i in s:
        #     dict[i] = dict.get(i, 0) + 1
        # for i in t:
        #     dict[i] = dict.get(i, 0) - 1
        #     if dict[i] < 0:
        #         return False
        # return True

        '''
        使用集合记录出现过的字符，遍历集合，计数是否相等（最佳！）
        '''
        if len(s) != len(t):
            return False
        set_s = set(s)
        if set_s == set(t):
            for i in set_s:
                if s.count(i) != t.count(i):
                    return False
            return True
        else:
            return False

s = "rat"
t = "car"
print(isAnagram(s, t))