class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        sub=""
        maxx=0
        seen= set()
        l=0
        for r in range(len(s)):
            char=s[r]
            while char in seen:
                seen.remove(s[l])
                l+=1
            
            seen.add(char)
            maxx=max(maxx,r-l+1)
        return maxx