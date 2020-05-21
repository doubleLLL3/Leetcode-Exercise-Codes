def myAtoi(str):
        '''
        1.一直遍历到不是空格，
        2.开始判断是否是有效数字或者正负号
        3.一直遍历到不是数字为止，判断数字大小
        '''
        if str == '':
            return 0

        for i in range(len(str)):
            if str[i] != ' ':
                break
                
        str2 = ''
        if str[i] == '+' or str[i] == '-':
            str2 += str[i]
            i += 1
       
        for j in range(i,len(str)):
            if str[j].isdigit():
                str2 += str[j]
            else:
                break

        if str2 == '':
            return 0
        if str2[0] == '-':
            if len(str2) > 1:
                return int(str2) if -int(str2) < (1<<31) else -(1<<31)  # int(str2)可以直接转换str里的正负号
            else:
                return 0
            
        elif str2[0] == '+':
            if len(str2) > 1:
                return int(str2) if int(str2) < (1<<31)-1 else (1<<31)-1
            else:
                return 0
        else:
            return int(str2) if int(str2) < (1<<31)-1 else (1<<31)-1

print(myAtoi("+-2"))
print(myAtoi(""))
print(myAtoi("words and 987"))
print(myAtoi("   -42"))
print(myAtoi("-91283472332"))
print(myAtoi(""))
