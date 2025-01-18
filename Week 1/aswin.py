par = '({['
ver = '({}[])'

def valid(par):
    dict1 = {'(': ')', '{': '}', '[': ']'} 
    stack = []

    for i in par:
        if i in dict1:
            stack.append(dict1[i])
        elif stack and i == stack[-1]:
            stack.pop()
        else:
            return False
    return not stack


p = valid(ver)
print(p)