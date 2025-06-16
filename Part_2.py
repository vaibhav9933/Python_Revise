#Strings
"""
str1 = "hello bro.\nhow are you"
str2 = 'ApnaCollege'

print(str1)"""
#concatenation
"""
str1 = "apna\t"
str2 = "collage"
final_str = str1 + str2

print(final_str)"""

#len()
"""
str1 = "Vaibhav"
print(len(str1))
"""

#indexing
"""
str = "apna College"
print(str[3])
"""

#slicing
"""
str = "ApnaCollege"
print(str[:4])
print(str[1:4])
print(str[4:])
print(str[-7: ])"""

#Practice
#wap to input user's name & print its length.
"""
a = input("Enter User First name:")
print(len(a))
"""
#wap to find the occurance of '$' in a string
"""
str = "hi, $ i am the the vaibhav$ from $"
print(str.count("$"))"""

# Conditional Statements
"""
age = 16
if (age>= 18):
    print("You can applay for licence")
else:
    print("you can't applay for licence") """

"""
num = 5
if(num > 2):
    print("Greater then 2")
elif(num>3):
    print("Greater then 3") """

"""

marks = int(input("Enter Students marks: "))
if(marks >= 90):
    grade = "A"
elif (marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70  and marks < 80):
    grade = "C"
else:
    grade ="D"
print("Grade of the studnets:",grade) """


#wap to chack if a number entered by the user is odd or even
"""
num = int(input("Enter the number:"))
rem = num % 2
if(rem == 0):
    print("Even")
else:
    print("odd")"""

#wap to find the grater of 3 numbers enterd by the user.
"""
num1 = int(input("Enter num 1:"))
num2 = int(input("Enter num 2:"))
num3 = int(input("Enter num 3:"))

if(num1 >= num2 and num1 >= num3):
    print("Num 1 is greater which is",num1)
elif(num2 >= num3):
    print("Num 2 is grater which is ",num2)
elif(num3 >= num1 and num3 >= num2):
    print("Num 3 is grater which is",num3)
else:
    print("Invalid input")"""

#wwap to check if a number is a multiple of 7 or not

"""
num = int(input("Enter number"))
if(num % 7 == 0):
    print("Multiple of ",num)
else:
    print("not a multiple") """

