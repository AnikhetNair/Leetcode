class Solution:
    def sumOfUnique(self, nums):
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
        total = 0
        for num, count in counts.items():
            if count == 1:
                total += num
        return total