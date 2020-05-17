def plusOne(digits):
        '''
        主要是要考虑到进位的问题？
        1.使用递归的方式，当需要进位时，将数组拆分成最后一个元素和其余元素两部分
        2.考虑其余元素是否需要拆分，继续
        '''
        # if digits[-1] <= 8:
        #     digits[-1] += 1
        #     return digits
        # elif len(digits) == 1:
        #     return [1,0]
        # else:
        #     return plusOne(digits[0:-1]) + [0]

        for i in range(len(digits)-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits.insert(0,1)
        return digits


print(plusOne([9,9]))