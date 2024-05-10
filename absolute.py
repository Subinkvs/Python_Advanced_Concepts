def diff(a,b):
    if (z := a - b)  < 0:
        return -z
    else:
        return z
print(diff(3, 7))