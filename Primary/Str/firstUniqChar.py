def firstUniqChar(s):
        '''
        1.将字符串放到字典里，key放字符，v放个数
        2.遍历字符串，找对应的v值，如果=1，则输出对应的索引
        3.如果不存在，则输出-1
        '''
        dict = {}
        for i in s:
            dict[i] = dict.get(i, 0) + 1
        for i,v in enumerate(s):
            if dict[v] == 1:
                return i
        return -1

firstUniqChar("loveleetcode")