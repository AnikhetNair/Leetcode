class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.sort()
        del salary[0]
        del salary[-1]
        k=sum(salary)
        return float(k)/len(salary)
        