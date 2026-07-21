class Solution(object):
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)

        window_size = n - k
        window_sum = sum(cardPoints[:window_size])
        min_sum = window_sum

        for right in range(window_size, n):
            window_sum += cardPoints[right] - cardPoints[right - window_size]
            min_sum = min(min_sum, window_sum)

        return sum(cardPoints) - min_sum