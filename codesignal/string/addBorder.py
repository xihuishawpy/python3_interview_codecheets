"""
For
picture = ["abc",
           "ded"]
the output should be
addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
"""
def addBorder(picture):
    b = '*'*(len(picture[0])+2)
    rtn = [b]
    rtn.extend(f'*{p}*' for p in picture)
    rtn.append(b)
    return rtn