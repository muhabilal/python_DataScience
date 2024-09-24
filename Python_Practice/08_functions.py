def greet_user():
    print("Hello, Users!")
greet_user()

def aoa(name):
    print(f"hello, {name}")
aoa("Bilal")

def myFun(name="khuda k bandy"):
    print(f"Hello,{name}")
myFun("Ali")


#return values
def square(number):
    return number*number

print(square(2))


#Recursion
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

#lamda function
x=lambda a:a+10
print(x(5))

y=lambda a,b: a*b
print(y(2,8))