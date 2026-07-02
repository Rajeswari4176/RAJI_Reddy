# All Formula Expressions in One Program

a = 10
b = 20
c = 30

length = 8
breadth = 5
height = 10
radius = 7
base = 12
side = 6
pi = 3.14159

print("Addition =", a + b)
print("Subtraction =", b - a)
print("Multiplication =", a * b)
print("Division =", b / a)
print("Modulus =", b % a)
print("Power =", a ** 2)
print("Average =", (a + b + c) / 3)

# Rectangle
print("Area of Rectangle =", length * breadth)
print("Perimeter of Rectangle =", 2 * (length + breadth))

# Square
print("Area of Square =", side * side)
print("Perimeter of Square =", 4 * side)

# Circle
print("Area of Circle =", pi * radius * radius)
print("Circumference of Circle =", 2 * pi * radius)

# Triangle
print("Area of Triangle =", 0.5 * base * height)

# Cube
print("Volume of Cube =", side ** 3)
print("Surface Area of Cube =", 6 * side * side)

# Cuboid
print("Volume of Cuboid =", length * breadth * height)
print("Surface Area of Cuboid =", 2 * (length * breadth + breadth * height + height * length))

# Simple Interest
P = 10000
R = 5
T = 2
print("Simple Interest =", (P * R * T) / 100)

# Celsius to Fahrenheit
celsius = 25
print("Fahrenheit =", (celsius * 9 / 5) + 32)

# Fahrenheit to Celsius
fahrenheit = 98.6
print("Celsius =", (fahrenheit - 32) * 5 / 9)

# Swap Two Numbers
x = 5
y = 10
x, y = y, x
print("After Swapping:", x, y)

# Even or Odd
num = 15
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Greatest of Three Numbers
largest = max(a, b, c)
print("Largest =", largest)

# Percentage
total = 600
marks = 510
print("Percentage =", (marks / total) * 100)