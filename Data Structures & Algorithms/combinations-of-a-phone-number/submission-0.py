class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}
        res=[]
        if not digits:
            return []
        n=len(digits)

        def back(curr,index):
            if index==n:
                res.append("".join(curr))
                return
            
            posibilities= m[digits[index]]
            for char in posibilities:
                curr.append(char)
                back(curr,index+1)
                curr.pop()
        back([],0)
        return res

