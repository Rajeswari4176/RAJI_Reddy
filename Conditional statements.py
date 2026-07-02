# 1. Print given value is positive or not
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 2. Check given character is Uppercase or Lowercase
# (Without using built-in functions)

ch = input("Enter a character: ")

if ch >= 'A' and ch <= 'Z':
    print("Uppercase")
elif ch >= 'a' and ch <= 'z':
    print("Lowercase")
else:
    print("Not an Alphabet")


# 3. Pass or Fail (6 Subjects)
s1 = int(input("Enter Subject 1 Marks: "))
s2 = int(input("Enter Subject 2 Marks: "))
s3 = int(input("Enter Subject 3 Marks: "))
s4 = int(input("Enter Subject 4 Marks: "))
s5 = int(input("Enter Subject 5 Marks: "))
s6 = int(input("Enter Subject 6 Marks: "))

if s1 >= 35 and s2 >= 35 and s3 >= 35 and s4 >= 35 and s5 >= 35 and s6 >= 35:
    print("PASS")
else:
    print("FAIL")