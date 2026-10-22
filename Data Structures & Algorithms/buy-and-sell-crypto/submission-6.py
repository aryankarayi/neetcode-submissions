class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        differences = []
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                differences.append(prices[j] - prices[i])
        if max(differences, default=-1) < 0:
            return 0
        else:
            return max(differences)

        