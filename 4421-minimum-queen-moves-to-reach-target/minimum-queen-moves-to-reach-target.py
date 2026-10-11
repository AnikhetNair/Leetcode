class Solution(object):
    def minQueenMoves(self, source, target):
        """
        :type source: List[int]
        :type target: List[int]
        :rtype: int
        """
        X=source[0]==target[0]
        Y=source[1]==target[1]

        if X and Y: return 0
        if X or Y:return 1
        if abs(source[0] - target[0]) == abs(source[1] - target[1]): return 1
        return 2
        