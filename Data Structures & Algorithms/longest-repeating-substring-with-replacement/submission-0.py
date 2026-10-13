class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxx=0
        l=0
        count=Counter(dict.fromkeys(s,0))
        for r in range(0,len(s)):
            char=s[r]
            wlength=r-l+1
            count[char]+=1
            while wlength-max(count.values())>k:
                lchar= s[l]
                count[lchar]-=1
                l+=1
                wlength-=1
            maxx=max(maxx,wlength)
        return maxx





                        
        