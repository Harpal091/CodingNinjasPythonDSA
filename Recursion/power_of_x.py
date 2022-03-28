def power_of_x(x,n):
    if n==0:
        return 1
    smallOp=power_of_x(x,n-1)
    Op= x* smallOp
    return Op

a=int(input())
b=int(input())
print(power_of_x(a,b))