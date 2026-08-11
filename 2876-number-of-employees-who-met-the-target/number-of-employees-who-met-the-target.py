class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        
        return sum(1 for h in hours if h >= target)