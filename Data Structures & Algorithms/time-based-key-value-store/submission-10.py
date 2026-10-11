class TimeMap:

    def __init__(self):
        self.data={}
        self.limits={}
    def set(self, key: str, value: str, timestamp: int) -> None:
        try:
            self.data[key].append([timestamp,value])
            self.limits[key]=(self.limits[key][0], timestamp)
        except:
            self.data[key]=[[timestamp,value]]
            self.limits[key]=(timestamp,timestamp)

    def get(self, key: str, timestamp: int) -> str:
        try:
            v_t= self.data[key]
        except:
            return ""        
        l,r=0,len(v_t)-1
        while l<=r:
            mid=(l+r)//2
            time= v_t[mid][0]
            if time > timestamp:
                r=mid-1
            else:
                l=mid+1
        time=v_t[(l+r)//2][0]
        return v_t[(l+r)//2][1] if time <= timestamp else ""
            
            



