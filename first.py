def fact(n):
    if n == 1:
        return 1
    return fact(n-1)*n


def ini(n):
    return [x for x in range(n)]


print(fact(5))
print(ini(4))

