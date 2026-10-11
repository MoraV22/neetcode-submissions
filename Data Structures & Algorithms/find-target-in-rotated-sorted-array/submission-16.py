class Solution:
    def findMin(self, nums: List[int]) -> int:
            if len(nums) == 1:
                return nums[0]
            left = 0
            right = len(nums)-1
            while left < right:
                mid = (left+right)//2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            return left
        
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            return 0 if nums[0]==target else -1
        minn= self.findMin(nums)
        n= len(nums)
        rotation= n-1-minn
        arr= nums+nums
        arr= arr[minn:minn+n]
        l,r= 0, n-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==target:
                return (mid +minn)%n
            elif arr[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return -1