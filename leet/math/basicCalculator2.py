"""
Basic Calculator II
"""
class Solution:
    def calculate(self, s: str) -> int:
        s += '$'
        sign = '+'
        i = num = 0
        stk = []

        while i < len(s):
            c = s[i]
            i += 1
            if c == " ":
                continue
            elif c.isdigit():
                num = num * 10 + int(c)
            else:
                if sign == '*':
                    stk.append(stk.pop() * num)
                elif sign == '+':
                    stk.append(num)
                elif sign == '-':
                    stk.append(-num)
                elif sign == '/':
                    stk.append(int(stk.pop() / num))

                sign = c
                num = 0
        return sum(stk)
        