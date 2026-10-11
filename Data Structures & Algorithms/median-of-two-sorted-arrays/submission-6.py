class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr= nums1+nums2
        arr.sort()
        k=len(arr)-1
        mid=k//2
        print(k,arr)
        if (k+1)%2==1:
            return arr[mid]
        else:
            return (arr[mid]+arr[mid+1])/2
