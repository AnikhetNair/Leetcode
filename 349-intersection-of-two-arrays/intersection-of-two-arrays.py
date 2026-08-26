class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        k=len(nums1)
        l=len(nums2)
        j=[]
        if k<l:
            for i in range(k):
                if nums1[i]  in nums2:
                    j.append(nums1[i])
        else:
            for i in range(l):
                if nums2[i]  in nums1:
                    j.append(nums2[i])
        return list(set(j))

        

        