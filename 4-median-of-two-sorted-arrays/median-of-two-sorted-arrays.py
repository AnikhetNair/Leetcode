class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)

        if m <= n:
            for i in range(m):
                nums2.append(nums1[i])
            nums2.sort()
            if (m + n) % 2 != 0:
                return nums2[(m + n) // 2]
            else:
                return (nums2[(m + n) // 2] + nums2[(m + n) // 2 - 1]) / 2.0
        else:
            for i in range(n):
                nums1.append(nums2[i])

            # Deducted outside the loop so it handles empty nums2 (n = 0)
            nums1.sort()
            if (m + n) % 2 != 0:
                return nums1[(m + n) // 2]
            else:
                return (nums1[(m + n) // 2] + nums1[(m + n) // 2 - 1]) / 2.0