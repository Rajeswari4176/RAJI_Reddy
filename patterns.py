# Armstrong Number

num = int(input("Enter a number: "))

temp = num
length = len(str(num))   # Find length of number
sum = 0

while temp > 0:
    digit = temp % 10          # Separate each digit
    sum = sum + digit ** length # digit^length
    temp = temp // 10

# Check condition
if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is Not an Armstrong Number")