#question 1
num = int(input("Enter a number:"))
if(num%2==0):
    print("The number is even")
else:
    print("The number is odd")
#question 2
import decimal
i=2
while(i<=10):
    print(float(1/i))
    i=i+1
#question 3
num = int(input("Enter a number:"))
print("The sequence of numbers until 0 is:")
while(num>=0):
    print(num,' ',end='')
    num=num-1
#question 4
from datetime import datetime
time = datetime.now()
string = time.strftime("%d/%m/%Y %H:%M:%S")
print(string)
#question 5
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
if(a>b and a>c):
    print(f"{a} is greater than {b} and {c}")
elif(b>a and b>c):
    print(f"{b} is greater than {a} and {c}")
else:
    print(f"{c} is greater than {a} and {b}")
#question 6
temp = int(input("Enter your temp:"))
inp = int(input("Enter to convert temp into 1.celsius 2.fahrenheit"))
if(inp==2):
    fh=((temp * 9/5) + 32)
    print("The converted temp in fh is:",fh)
else:
    ce=(temp-32) * (5/9)
    print("The converted temp in degree celsius is:",ce)
#question 7
i=20
while(i>0):
    if(i==2 or i==3 or i==5 or i==7):
        print(f"{i} is a prime number")
    elif((i%2!=0 and i!=2) and i%3!=0 and i%5!=0 and i%7!=0):
        print(f"{i} is a prime number")
    else:
        print(f"{i} is not a prime number")
        i=i-1
#question 8
import math
a = int(input("Enter the first side length:"))
b = int(input("Enter the second side length:"))
c = int(input("Enter the third side length:"))
sab = math.sqrt(a*a + b*b)
sbc = math.sqrt(b*b + c*c)
sac = math.sqrt(a*a + c*c)
if((sab==c) or (sbc==a) or (sac==b)):
    print("Yes, this is a right-angle triangle")
else:
    print("No, it is not a right-angle triangle")
#question 9
a = int(input("Enter marks for test1:"))
b = int(input("Enter marks for test2:"))
c = int(input("Enter marks for test3:"))
large=0
slarge=0
if(a>b and a>c):
    large=a
elif(b>a and b>c):
    large=b
else:
    large=c
if(a==large and b>c):
    slarge=b
else:
    slarge=c
if(b==large and a>c):
    slarge=a
else:
    slarge=c
if(c==large and a>b):
    slarge=a
else:
    slarge=b
print("The average of best two test marks is:",(large+slarge)/2)
#question 10
num = int(input("Enter a number: "))
temp = num
temp2 = str(num)
rev = 0
while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if temp == rev:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
i = 0
while i < len(temp2):
    print(f"{temp2[i]} appears {temp2.count(temp2[i])} times")
    i += 1
#question 11
string = input("Enter a sentence:")
i=0
upper=0
lower=0
num=0
while i<len(string):
    if(string[i].isupper()):
        upper=upper+1
    elif(string[i].islower()):
        lower=lower+1
    elif(string[i].isdigit()):
        num=num+1
i=i+1
print("The uppercase char present in string are:",upper)
print("The lowercase char present in string are:",lower)
print("\nThe numbers present in string are:",num)