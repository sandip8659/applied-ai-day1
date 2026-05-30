a=int(input("enter the first number "))
b=int(input("enter 2nd number "))
choose=input("enter the operation perform + ,_-,*,/")
if choose=="+":
    print("the sum is ",a+b)
elif choose=="-":
    print("the difference is ".a-b)
elif choose=="*":
    print ("the multiplication is ".a*b)
elif choose =="/":
    print("the division is ",a/b)
else: print ("invalid input try again ")