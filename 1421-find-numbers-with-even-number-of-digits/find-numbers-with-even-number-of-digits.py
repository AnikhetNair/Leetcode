class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for k in nums:
            if (k>=10 and k<100) or (k>=1000 and k<10000)or k>=100000:
                count+=1
        return count
        