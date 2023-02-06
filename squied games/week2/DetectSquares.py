class DetectSquares:

    def __init__(self):
        self.freq = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.freq[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x,y = point
        result = 0
        points = list(self.freq.keys())
        for a,b in points:
            if x == a and y != b:
                ln = y - b

                result += self.freq[(a,b)] * self.freq[(x+ln,y)] * self.freq[(x+ln, b)]
                result += self.freq[(a,b)] * self.freq[(x-ln,y)] * self.freq[(x-ln, b)]
        
        return result



