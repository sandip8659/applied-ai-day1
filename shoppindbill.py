a=int(input("enter the price of the 1st item: "))
b=int(input("enter the price of the 2nd item: "))
c=int(input("enter the price of the 3rd item: "))
d=int(input("enter the price of the 4th item: "))
e=int(input("enter the price of the 5th item: "))
f=int(input("enter the price of the 6th item: "))
g=int(input("enter the price of the 7th item: "))
h=int(input("enter the price of the 8th item: "))
i=int(input("enter the price of the 9th item: "))
j=int(input("enter the price of the 10th item: "))
total=a+b+c+d+e+f+g+h+i+j
print("The total price of the 10 items is:", total)
discount=total*0.1
final_price=total-discount
print("The final price after applying a 10% discount is:", final_price)
