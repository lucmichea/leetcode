import numpy as np

class Point(object):

    def __init__(self, x1, y1, z1):
        self.x = x1
        self.y = y1
        self.z = z1

    def distance(self,p):
        return self.x - p.x + self.y - p.y + self.z - p.z

class Vector(object):

    def __init__(self, start_pt, end_pt):
        self.vx = end_pt.x - start_pt.x
        self.vy = end_pt.y - start_pt.y
        self.vz = end_pt.z - start_pt.z

    def normalize(self):
        n = self.norm()
        self.vx = self.vx / n
        self.vy = self.vy / n
        self.vz = self.vy / n
    
    def norm(self):
        return np.sqrt(self.vx**2 + self.vy**2 + self.vz**2)

    def __str__(self):
        return str([self.vx, self.vy, self.vz])

    @staticmethod
    def give_name(name):
        name = name


if __name__ == "__main__":
    p = Point(2,1,4)
    p1 = Point(1,4,5)
    print(p.distance(p1))
    v = Vector(p,p1)
    v.normalize()
    print(v)
    v.give_name('aaaa')
    print(v.name)