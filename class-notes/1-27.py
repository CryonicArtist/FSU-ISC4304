def add(a,b):
    return a+b
def sub(a,b):
    return a-b

#v = add
#v(3,4)
#v = sub
#v(3,4)

#v = [sub, add]
#for i in v:
#    print(i(5,9))
    
#def calc(fct, a, b):
    return fct(a,b)
#v = [add, sub]
#for i in v:
    print(calc(i, 5,8))

#fct = lambda x,y: x+7
#fct(3,4)

#def factorial(n):
    if(n <= 1):
        return 1
    else:
        return n*factorial(n-1)
    
#print(factorial(3))
#print(factorial(10))
#print(factorial(9))

#Fibonacchi Sequence
#def fib(n):
    if n==1:
        return 1
    if n==0:
        return 0
    return fib(n-2) + fib(n-1)

#if __name__=='__main__':
    for i in range(11):
        print(fib(i), end=' ')
        