class Solution(object):
    def dist(self,n1,n2):
        x=(n1[0]-n2[0])**2
        y=(n1[1]-n2[1])**2
        return (x+y)**0.5
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        l=[
            self.dist(p1,p2),
            self.dist(p2,p3),
            self.dist(p3,p4),
            self.dist(p4,p1),
            self.dist(p2,p4),
            self.dist(p1,p3)
        ]
        l.sort()
        return (l[0]>0 and l[0]==l[1]==l[2]==l[3] and l[4]==l[5]

        )
        