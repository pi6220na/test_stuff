def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


def fib(n):
    print('n = {}  (n-1) = {}  (n-2) = {}  sum = {}'.format(n, (n-1), (n-2), (n-1)+(n-2)))
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


fib = memoize(fib)

print(fib(5))