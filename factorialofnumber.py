a=int(input("Enter a number: "))
if a>0:
    factorial=1
    for i in range(1,a+1):
     factorial=factorial*i
print("the factorial of",a,"is",factorial)
