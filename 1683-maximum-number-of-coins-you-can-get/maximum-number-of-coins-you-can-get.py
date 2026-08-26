class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
      
        piles.sort()
        
        return sum(piles[len(piles) // 3 :: 2])
        