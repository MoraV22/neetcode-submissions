import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones= [-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            a,b = -heapq.heappop(stones),-heapq.heappop(stones)
            
            if a==b:
                continue
            else:
                heapq.heappush(stones,-abs(a-b))
        return -stones[0] if stones else 0
