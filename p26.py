def reciprocal(d):
    list = []
    r = 1
    while r != 0:
        r = r * 10 % d
        for i in range(len(list)):
            if list[i] == r:
                return len(list) - i
        list.append(r)
        
    return 0

t = 0
target = 0
for d in range(1, 1001):
    l = reciprocal(d)
    if t < l:
        t = l
        target = d
        
print(target)
