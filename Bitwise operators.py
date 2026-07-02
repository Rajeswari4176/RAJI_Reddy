# Bitwise Operators Practice

a = 10      # 1010
b = 10      # 1010
c = 5       # 0101

print("a =", a)
print("b =", b)
print("c =", c)

# 1. XOR (^)
print("\nXOR Operator")
print("a ^ b =", a ^ b)      # Same values
print("a ^ c =", a ^ c)      # Different values

# 2. AND (&)
print("\nAND Operator")
print("a & b =", a & b)
print("a & c =", a & c)

# 3. OR (|)
print("\nOR Operator")
print("a | b =", a | b)
print("a | c =", a | c)

# 4. NOT (~)
print("\nNOT Operator")
print("~a =", ~a)

# 5. Left Shift (<<)
print("\nLeft Shift")
print("a << 1 =", a << 1)
print("a << 2 =", a << 2)

# 6. Right Shift (>>)
print("\nRight Shift")
print("a >> 1 =", a >> 1)
print("a >> 2 =", a >> 2)

# Check Even or Odd using AND
num = 8

print("\nEven or Odd using AND")
if num & 1:
    print(num, "is Odd")
else:
    print(num, "is Even")