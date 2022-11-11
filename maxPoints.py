class Solution:
    def gcd(self, a, b):
        if a < b:
            a,b = b,a

        if b == 0:
            return a

        return self.gcd(a%b, b)
        
    def get_fraction(self, up, down):
        sign = -1 if up*down < 0 else 1
        up = abs(up)
        down = abs(down)
        
        g = self.gcd(up, down)
        
        up *= sign 
        return (up//g, down//g)
    
    def get_slope(self, p1, p2):
        a,b = p1
        x,y = p2
        
        up = y - b
        down = x - a
        
        if up == 0:
            return 0
        
        if down == 0:
            return "inf"

        return self.get_fraction(up,down)
    
        
    def get_intercept(self, point, slope):
        a,b = point
        x,y =  slope   
        
        up = x*a - b*y
        down = x
        
        
        if down == 0:
            return "inf"
        
        if up == 0:
            return 0
        
        return self.get_fraction(up,down)
        
    def maxPoints(self, points: List[List[int]]) -> int:
        
        if len(points) == 1:
            return 1
        
        lines = defaultdict(set)
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                p1 = points[i]
                p2 = points[j]
                
                slope = self.get_slope(p1, p2)
                
                if slope == 0 or slope == "inf":
                    # if sope == 0 -- orizontal 
                    # if slope == "inf" -- vertial
                    x = ("inf", p1[1]) if slope == 0 else p1[0]
                    
                else:
                    x = self.get_intercept(p1, slope)
                node = (slope, x)
                
                lines[node].add(tuple(p1))
                lines[node].add(tuple(p2))
        
            
        return max(map(len, lines.values()))
