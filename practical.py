a = []
l = int(input("how many students in a"))
for i in range(l):
    num = int(input("enter no."))
    a.append(num)
    
b = []
m = int(input("how many students in b"))
for i in range(m):
    num1 = int(input("enter no."))
    b.append(num1)

c = []
n = int(input("how many students in c"))
for i in range(n):
    num2 = int(input("enter no."))
    c.append(num2)

def union(a,b):
    res = list(a)
    for i in b:
        if i not in a:
            res.append(i)
    return f"union is {res}"

def intersect(a,b):
    res = []
    for i in a:
        if i in b:
            res.append(i)
    return f"intersection is {res}"

def either(a,b):
    u = union(a,b)
    i = intersect(a,b)
    for value in i:
        u.remove(value)
    return f"either is {u}"

def minus(a,b):
    res = list(a)
    for i in b:
        if i in res:
            res.remove(i)
    return f"sub is {res}"

union(a,b)
intersect(a,b)
either(a,b)
minus(a,b)
