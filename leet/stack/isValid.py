class Solution:
    def isValid(self, s: str) -> bool:
        while '[]' in s or '()' in s or '{}' in s:
            s = s.replace('[]','').replace('()','').replace('{}','')
        return not s


"""
time: 10 min
time: O(n)
space: O(n)
errors:
lower case values/keys
Have to use stack because 3 charactors open/close
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        mp = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c in mp.values():
                stk.append(c)
            elif c in mp:
                test = stk.pop() if stk else '#'
                if mp[c] != test:
                    return False
        return not stk

                
class Solution:
    def isValid(self, s) -> bool:
        stk = []
        for c in s:
            if c == '(':
                stk.append(')')
            elif c == '[':
                stk.append(']')
            elif c == '{':
                stk.append('}')
            elif not stk or stk.pop() != c:
                return False
        return not stk