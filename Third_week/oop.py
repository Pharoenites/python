class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def coordinates(self):
        print(f'coordinates are: {self.x}, {self.y}')


my_point = Point(5, 16)
my_point.coordinates() 