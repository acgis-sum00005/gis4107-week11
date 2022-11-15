class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

class Line:
    def __init__(self, from_point, to_point):
        self.from_point = from_point
        self.to_point = to_point

    @property
    def length(self):
        self.__length = ((self.to_point.x - self.from_point.x) ** 2 + (self.to_point.y - self.from_point.y) ** 2) ** 0.5
        return self.__length

        
        
class Polyline:
    def __init__(self):
        self.__segments = []
        self.__length = float() 
    
    def add_segment (self, seg):
        self.__segments.append(seg)

    @property
    def length(self):
        self.__length = sum([seg.length for seg in self.__segments])
        return self.__length
