"""
给定两个整数，被除数dividend和除数divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数dividend除以除数divisor得到的商。
整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

示例1:
输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3

"""


class Solution:
    def divide(self, dividend, divisor):
        int_min, int_max = -2 ** 31, 2 ** 31 - 1
        # 被除数为最小值
        if dividend == int_min:
            if divisor == 1:
                return int_min
            if divisor == -1:
                return int_max
        # 除数为最小值
        if divisor == int_min:
            return 1 if dividend == int_min else 0
        # 被除数为0
        if dividend == 0:
            return 0

        # 类二分查找
        # 将所有正数取反数，这样就只需要考虑一种情况
        rev = False
        if dividend > 0:
            dividend = -dividend
            rev = not rev
        if divisor > 0:
            divisor = -divisor
            rev = not rev

        candidates = [divisor]
        # 注意溢出
        while candidates[-1] >= dividend - candidates[-1]:
            candidates.append(candidates[-1] + candidates[-1])

        ans = 0
        for i in range(len(candidates) - 1, -1, -1):
            if candidates[i] >= dividend:
                ans += (1 << i)
                dividend -= candidates[i]

        return -ans if rev else ans
