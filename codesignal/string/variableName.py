"""
For name = "var_1__Int", the output should be
variableName(name) = true;
For name = "qq-q", the output should be
variableName(name) = false;
"""

def variableName(name):
    if not name or name[0].isdigit():
        return False
    return not any(not c.isalnum() and c != '_' for c in name)

def variableName(name):
    return name.isidentifier()