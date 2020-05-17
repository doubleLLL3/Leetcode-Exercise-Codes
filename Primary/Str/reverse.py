def reverse(x):
        '''
        1.转成字符串，再进行反转后，转成数字输出。注意判断正负数、数字溢出
        '''
        def change(x, left, right):
            while left < right:
                x[left], x[right] = x[right], x[left]
                left += 1
                right -= 1
            return x
        
        if x < 0:
            x = -x
            x = list(str(x))
            x = change(x, 0, len(x)-1)
            if int(''.join(x)) <  2 ** 31:
                return -int(''.join(x))
        else:
            x = list(str(x))
            x = change(x, 0, len(x)-1)
            if int(''.join(x)) <  2 ** 31 - 1:
                return int(''.join(x))
        return 0

print(reverse(123))