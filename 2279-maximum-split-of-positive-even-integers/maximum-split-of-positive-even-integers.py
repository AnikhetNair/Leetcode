class Solution(object):
    def maximumEvenSplit(self, finalSum):
        """
        :type finalSum: int
        :rtype: List[int]
        """
        if finalSum % 2 != 0:
            return []

        res = []
        even = 2
        
        while finalSum >= even:
            res.append(even)
            finalSum -= even
            even += 2
        
        res[-1] += finalSum
        
        return res