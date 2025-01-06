dict1=dict(('()','{}','[]'))
par = '({['
ver = '({}[])'

def valid(par):
    res = []
    v = ''
    for i in par:
        if i in dict1:
            v += dict1[i]
        
        if i == v:
            res.append(i)
    
    return bool(res)

p = valid(ver)
print(p)