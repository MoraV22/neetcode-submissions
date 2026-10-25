class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        def bfs(curr):
            if len(curr)==n:
                res.append(curr[:])
                return
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    bfs(curr)
                    curr.pop()
        bfs([])
        return res
        
        