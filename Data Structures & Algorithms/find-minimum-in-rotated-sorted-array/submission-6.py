class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        if r==0:
            return nums[0]
        while l<=r:
            mid=(l+r)//2
            if nums[l]<nums[mid] and nums[r]<nums[mid]:
                l=mid
            elif nums[l]>nums[mid] and nums[mid]<nums[r]:
                r=mid
            elif nums[l]<nums[mid] and nums[mid]<nums[r]:
                return nums[l]
            elif l+1==r:
                return nums[l] if nums[l]<nums[r] else nums[r]
        