class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        sign = 1

        for digit in str(n):
            ans += int(digit) * sign
            sign *= -1

        return ans