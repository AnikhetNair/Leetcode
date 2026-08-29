class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        k=len(nums1)
        l=len(nums2)
        t=[]
        if k>l:
            for i in range(k):
                if nums1[i] in nums2:
                    t.append(nums1[i])
                    nums2.remove(nums1[i])
        else:
            for i in range(l):
                if nums2[i] in nums1:
                    t.append(nums2[i])
                    nums1.remove(nums2[i])
        return t

