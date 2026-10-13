class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        a=Counter(s1)
        a1= set(s1)
        a2=len(s1)
        l=0
        b=Counter()

        for r in range(len(s2)):
            if b==a:
                return True
            char=s2[r]
            b[char]+=1
            print(b,char)
            print(l,r)            
            
            while r-l+1>a2:
                lchar=s2[l]
                b[lchar]-=1
                l+=1
        return a==b

