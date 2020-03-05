def collatz(n):
    print(n, end=' ')
    if n == 1:
        return
    elif n%2 == 0:
        return collatz(n // 2)
    else:
        return collatz(3 * n + 1)

def test_fun(x,y):
    print(x,y)
    if x == y:
        return collatz(x)
    elif x > y:
        return test_fun(x - 1, y)
    else:
        return test_fun(x,y-1)

test_fun(3,4)
