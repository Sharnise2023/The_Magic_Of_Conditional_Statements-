num1 = ("5")
num2 = ("3")
num3 = ("7")

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print(f"The largest number is {largest}.")

# Task 2:
num1 = ("5")
num2 = ("3")
num2 = ("7")

# Find the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Find the smallest number
if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest= num2
else:
    smallest = num3
print(f"The smallest number is {smallest}.")
print(f"The largest number is {largest}.")
