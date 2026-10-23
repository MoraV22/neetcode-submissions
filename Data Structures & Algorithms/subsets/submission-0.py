class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def backtracking(current,index):
            nonlocal res
            if index==len(nums):
                res.append(current)
                return
            
            num= nums[index]
            backtracking(current.copy(),index+1)
            current.append(num)
            backtracking(current.copy(),index+1)
            
        
        backtracking([],0)
        return res