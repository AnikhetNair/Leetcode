class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        sm=0
        piles.sort()
        k=len(piles)//3
        for i in range(1,k+1):
            sm+=piles[-2*i]
        return sm
        