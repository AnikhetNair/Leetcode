class Solution(object):
    def minBishopMoves(self, source, target):
        """
        :type source: List[int]
        :type target: List[int]
        :rtype: int
        """
        if (sum(source)%2)==(sum(target)%2):
            if sum(source)==sum(target) or abs(source[0]-target[0])==abs(source[1]-target[1]):
                return 1
            return 2
        return -1
        