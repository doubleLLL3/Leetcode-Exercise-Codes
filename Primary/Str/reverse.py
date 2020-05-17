def reverse(x):
        '''
        1.转成字符串，再进行反转后，转成数字输出。注意判断正负数、数字溢出
        '''
        # def change(x, left, right):
        #     while left < right:
        #         x[left], x[right] = x[right], x[left]
        #         left += 1
        #         right -= 1
        #     return x
        
        # if x < 0:
        #     x = -x
        #     x = list(str(x))
        #     x = change(x, 0, len(x)-1)
        #     if int(''.join(x)) <  2 ** 31:
        #         return -int(''.join(x))
        # else:
        #     x = list(str(x))
        #     x = change(x, 0, len(x)-1)
        #     if int(''.join(x)) <  2 ** 31 - 1:
        #         return int(''.join(x))
        # return 0

        '''
        也是转为字符串
        '''
        # x=str(x)
        # x=[i for i in x]
        # tmp=0
        # if x[0]=='-':
        #     tmp=x.pop(0)
        # x.reverse() # 用这种方式反转列表
        # while x[0]==0:
        #     x.pop(0)
        # x="".join(x)
        # if tmp=='-':
        #     return int(tmp+x) if -2147483648 < int(tmp+x) else 0
        # else:
        #     return int(x) if int(x) < 2147483647 else 0

        '''
        用数学方式来做
        1.数字加绝对值(在python里带负号去取余或取整都不对)，然后每次把最后一位加到一个变量里，
        2.变量里做乘10运算，考虑溢出情况(移位表示)，直到原数字转为0
        '''
        res = 0
        abs_x = abs(x)
        boundry = (1<<31) -1 if x>0 else 1<<31 # 先写出来避免重复计算
        while abs_x > 0:
            res = res * 10 + abs_x % 10
            if res > boundry:
                return 0
            abs_x //= 10
        return res if x > 0 else -res     

print(reverse(1463847412))