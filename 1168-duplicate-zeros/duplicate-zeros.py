class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        k=[]
        for i in range(len(arr)):
            if arr[i]==0 and i==len(arr)-1:
                break
            if arr[i]==0:
                k.append(0)
            k.append(arr[i])
        for i in range(len(arr)):
            arr[i] = k[i]
        