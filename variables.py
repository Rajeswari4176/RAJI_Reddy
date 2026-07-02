# Python Input() and Output() Function Errors - All in One Program

# 1. Missing Quotes in input()
# Wrong:
# name = input(Enter your name:)

# Correct:
name = input("Enter your name: ")
print("Name:", name)

# 2. Missing Parentheses in print()
# Wrong:
# print name

# Correct:
print(name)

# 3. String and Integer Addition
# Wrong:
# print("Age is " + age + 1)

age = int(input("Enter your age: "))
print("Age after 1 year:", age + 1)

# 4. input() Returns String
# Wrong:
# a = input("Enter first number: ")
# b = input("Enter second number: ")
# print(a + b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)

# 5. Missing Closing Parenthesis
# Wrong:
# print("Hello"

print("Hello")

# 6. Undefined Variable
# Wrong:
# print(city)

city = "Hyderabad"
print("City:", city)

# 7. Wrong Data Type
# Wrong:
# print(num + "10")

num = int(input("Enter a number: "))
print("Number + 10 =", num + 10)

# 8. Wrong Input Conversion
# Wrong:
# marks = int(input("Enter marks: "))   # If input is 95.5

marks = float(input("Enter marks: "))
print("Marks:", marks)

# 9. Forgetting input()
# Wrong:
# name = "Enter your name: "

name = input("Enter your name again: ")
print("Welcome", name)

# 10. Multiple Inputs in One Line
# Wrong:
# a = int(input("Enter two numbers: "))
# b = int(input())

x, y = map(int, input("Enter two numbers: ").split())
print("First Number:", x)
print("Second Number:", y)
print("Addition:", x + y)