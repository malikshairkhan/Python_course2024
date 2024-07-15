"""num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

sum = num1 + num2

print(f"the sum of {num1} and {num2} is {sum}")"""

"""
num = int(input("Enter a number:"))

if num % 2 == 0:
    print(f"{num} is even ")
else:
    print(f"{num} is odd")    """
    
"""num1 = float(input("enter ist number"))
num2 = float(input("enter 2nd number"))
num3 = float(input("enter 3rd number"))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
    
else:
    largest = num3
print(f"the largest number among {num1},{num2}, and {num3} is {largest}")"""

# h = int(input("enter number"))
# a = int(input("enter number"))
# e = int(input("enetr number"))

# if ((h == 5 and a == 18)or(a == 18 and  e==12)or (e==12 and h==5)):
#     print("pass")
# else:
#     print("fail")
#total_number = 100
marks = int(input("Enter your marks: "))
 
# if (marks>=90):
#     print("you got A+")
# elif (marks>=80):
#     print("you got A")
# elif (marks>=70):
#     print("you got B+")
# elif (marks>=60):
#     print("you got B")
# else:
#     print("you got F")
    
if (marks>=90 and marks==100):
    print("you got A+")
elif (marks>=80 and marks<90):
    print("you got A")
elif (marks>=70 and marks<80):
    print("you got B+")
elif (marks>=60 and marks<70):
    print("you got B")
else:
    print("you got F")
    
