#без рекурсия
def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(10))

#с рекурсия
def recursive(n, a=0, b=1):
    if n==0:
        return a
    else:
        return recursive(n-1, b, a+b)
print(recursive(10))