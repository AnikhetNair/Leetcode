class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left=(len(nums)-1)//2
        right=len(nums)-1
        nums.sort()
        k=[]
        for i in range(len(nums)):
            if i%2==0:
                k.append(nums[left])
                left-=1
            else:
                k.append(nums[right])
                right-=1
        for i in range(len(nums)):
            nums[i]=k[i]
        