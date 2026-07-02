# 1. Sum of Digits
num = int(input("Enter a number: "))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit
    temp //= 10
print("Sum of Digits =", sum)

# -----------------------------------

# 2. Reverse a Number
num = int(input("\nEnter a number: "))
temp = num
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
print("Reverse =", reverse)

# -----------------------------------

# 3. Count Digits in a Number
num = int(input("\nEnter a number: "))
temp = num
count = 0
while temp > 0:
    count += 1
    temp //= 10
print("Number of Digits =", count)

# -----------------------------------

# 4. Check Even or Odd
num = int(input("\nEnter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# -----------------------------------

# 5. Check Prime Number
num = int(input("\nEnter a number: "))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")

# -----------------------------------

# 6. Find Factorial of a Number
num = int(input("\nEnter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial =", fact)

# -----------------------------------

# 7. Find Factors of a Number
num = int(input("\nEnter a number: "))
print("Factors are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
print()

# -----------------------------------

# 8. Check Palindrome Number
num = int(input("\nEnter a number: "))
temp = num
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

# -----------------------------------

# 9. Check Armstrong Number
num = int(input("\nEnter a number: "))
temp = num
length = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** length
    temp //= 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

# -----------------------------------

# 10. Find GCD (HCF) of Two Numbers
a = int(input("\nEnter First Number: "))
b = int(input("Enter Second Number: "))

gcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD =", gcd)