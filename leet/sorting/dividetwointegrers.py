"""
Divide Two Integers
O(logn)
O(logn)
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        MIN_INT = -2147483648       # -2**31

        if dividend == MIN_INT and divisor == -1:
            return 2147483647

        quotient = 0
        sign = 1
        if dividend < 0:
            sign *= -1
            dividend *= -1
        if divisor < 0:
            sign *= -1
            divisor *= -1        

        while dividend >= divisor:
            powerOfTwo = 1

            value = divisor
            while value + value <= dividend:
                value += value
                powerOfTwo += powerOfTwo

            dividend -= value
            quotient += powerOfTwo

        quotient = quotient * sign

        return quotient

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        MIN_INT = -2147483648       # -2**31

        if dividend == MIN_INT and divisor == -1:
            return 2147483647

        quotient = 0
        sign = 1
        if dividend < 0:
            sign *= -1
            dividend *= -1
        if divisor < 0:
            sign *= -1
            divisor *= -1        

        while dividend >= divisor:
            powerOfTwo = 1

            value = divisor
            while (value << 1) <= dividend:
                value <<= 1
                powerOfTwo <<= 1

            dividend -= value
            quotient += powerOfTwo

        quotient = quotient * sign

        return quotient