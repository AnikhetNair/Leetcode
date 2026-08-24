import itertools

class Solution(object):
    def stoneGameVIII(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        
        # Python 2 simulation of itertools.accumulate
        # Using a loop since accumulate is not available in Python 2
        s = []
        current_sum = 0
        for x in A:
            current_sum += x
            s.append(current_sum)

        # Python 2 manual memoization dictionary to replace @cache
        memo = {}

        def maxDiff(i):
            if i in memo:
                return memo[i]
            if i == n - 1: 
                return s[n - 1]
            
            # Compute and store the result
            res = max(maxDiff(i + 1), s[i] - maxDiff(i + 1))
            memo[i] = res
            return res

        return maxDiff(1)
