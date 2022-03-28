def fib(n):
    if n==0 or n==1:
        return 1
    fib_n1=fib(n-1)
    fib_n2=fib(n-2)
    Op=fib_n1+fib_n2
    return Op

print(fib(5))
print(fib(7))
print(fib(3))