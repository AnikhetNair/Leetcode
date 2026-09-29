class Solution(object):
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        on=(n+1)//2
        en=n//2

        om=(m+1)//2
        em=m//2

        return em*on+en*om
        