class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        c5=0
        c10=0
        c20=0
        for i in range(len(bills)):
            if bills[i]==5:
                c5+=1
            elif bills[i]==10:
                c5-=1
                c10+=1
            elif bills[i]==20:
                if c5>=1 and c10>=1:
                    c5-=1
                    c10-=1
                    c20+=1
                    continue
                elif c5>=3:
                    c5-=3
                    c20+=1
                    continue
                return False
            if c5<0 or c10<0 or c20<0:
                return False
        return True
        