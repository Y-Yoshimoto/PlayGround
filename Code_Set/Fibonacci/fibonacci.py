# coding:UTF-8
# Lambda式
fib = lambda n: fib(n-2)+fib(n-1) if n > 1 else(1 if n == 1 else 0)


fibList = [fib(i) for i in range(10)]

print fibList

'''
#　関数
def fib(n):
    if n > 1:
        return fib(n-2) + fib(n-1)
    elif n == 1:
        return 1
    else:
        return 0
'''
