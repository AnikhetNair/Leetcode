class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        a = min(min_idx, max_idx)
        b = max(min_idx, max_idx)
        both_from_front = b + 1
        both_from_back = n - a
        mixed = (a + 1) + (n - b)
        
        return min(both_from_front, both_from_back, mixed)

        