class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0

        for i in range(1, 11):
            if i * k <= num and (num - i * k) % 10 == 0:
                return i

        return -1