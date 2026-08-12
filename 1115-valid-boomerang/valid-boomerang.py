class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        # Unpack the three coordinates
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        
        # Calculate the cross multiplication to check for collinearity
        # If both sides are equal, the points are on the same line (returns False)
        return (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1)
