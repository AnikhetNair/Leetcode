class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = Counter(nums)
        return [num for num, count in counts.items() if count == 1]

