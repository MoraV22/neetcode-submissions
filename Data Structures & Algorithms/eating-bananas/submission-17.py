class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if sum(piles)<=h:
            return 1
        l,r= 2, max(piles)
        mid=0
        while l<r:
            mid=(l+r)//2
            times= sum(math.ceil(x/mid) for x in piles)
            print(l,r)
            print(mid,times)
            if times>h:
                l=mid+1
            else:
                r=mid
        return (l+r)//2