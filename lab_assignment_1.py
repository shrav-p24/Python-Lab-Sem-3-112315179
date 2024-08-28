import sys
import keyword
import math
print(sys.version)
print(keyword.kwlist)
name = input("Enter your name:")
age = int(input("Enter your age:"))
after_age = (100-age) + 2024
print(f"{name}, the year that you will turn 100 is: {after_age}")
radius = int(input("Enter the radius of the circle:"))
area = (math.pi)*radius*radius
circumference = (math.pi)*2*radius
print("The area of circle is:",area)
print(f"The circumference of the circle is: {circumference:.4f}")
user_input = int(input("Enter an even or odd number:"))
if(user_input %2 == 0):
    print("The given number",user_input,"is even")
else:
    print("The given number",user_input,"is odd")
if(0.1+0.2==0.3):
    print("True")
else:
    print("False")
#As the above 0.1+0.2 is false, we need to convert them into the same type to
value = int(0.1) + int(0.2) == int(0.3)
print(value)
name = "python"
name2 = "lab"
new_string = name + " " + name2
print(new_string)
swap1 = name2[0:2] + name[2:]
swap2 = name[0:2] + name2[2:]
re_string = swap1 + " " + swap2
print(re_string)
name = input("Enter a string including lowercase, uppercase, digits and underscore to check whether the given string is an identifier or not:")
print("The keywords, variables beginning with numbers, special symbols aren't allowed in identifiers")
if(name.isidentifier()):
 print("Yes, the given string",name,"can be used as an identifier")
else:
 print("No,",name,"cannot be used as an identifier")
name = input("Enter a string:")
new_string = name[-1] + name[1:-1] + name[0]
print("The new string with first and last characters swapped is:",new_string)
user_input = input("Enter a string to be displayed in upper and lowercase:")
print("The given string is:",user_input)
print("The string in uppercase is:",user_input.upper())
print("The string in lowercase is:",user_input.lower())