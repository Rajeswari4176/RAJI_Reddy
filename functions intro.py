from typing import List

# -----------------------------------------
# 2544. Alternating Digit Sum
# -----------------------------------------

class Solution1:
    def alternateDigitSum(self, n: int) -> int:
        digits = str(n)
        ans = 0

        for i in range(len(digits)):
            if i % 2 == 0:
                ans += int(digits[i])
            else:
                ans -= int(digits[i])

        return ans


# Example
obj1 = Solution1()
print("2544. Alternating Digit Sum")
print(obj1.alternateDigitSum(521))      # Output: 4


# -----------------------------------------
# 2553. Separate the Digits in an Array
# -----------------------------------------

class Solution2:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            for digit in str(num):
                ans.append(int(digit))

        return ans


# Example
obj2 = Solution2()
print("\n2553. Separate the Digits in an Array")
print(obj2.separateDigits([13, 25, 83, 77]))   # Output: [1, 3, 2, 5, 8, 3, 7, 7]