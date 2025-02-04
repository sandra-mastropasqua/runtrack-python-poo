class Point :
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Point({self.x}, {self.y})")
    
    def afficherX(self):
        print(f"X:{self.x}")
    
    def afficherY(self):
        print(f"Y:{self.y}")
    
    def changerX(self, new_x):
        self.x = new_x
    
    def changerY(self, new_y):
        self.y = new_y

point1 = Point(3, 4)
point1.afficherLesPoints()
point1.afficherX()
point1.afficherY()
point1.changerX(10)
point1.changerY(20)
point1.afficherLesPoints()