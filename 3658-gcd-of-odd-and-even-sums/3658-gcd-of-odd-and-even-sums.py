from math import gcd

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = 0
        sumEven = 0

        for i in range(1, n + 1):
            sumOdd += 2 * i - 1
            sumEven += 2 * i

        return gcd(sumOdd, sumEven)