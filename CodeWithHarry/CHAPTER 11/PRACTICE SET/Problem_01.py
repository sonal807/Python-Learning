#Create a class (2-D vector) and use it to create another class representing 3-D vector.
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"2D vector: {self.x}x, {self.y}y")

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def show(self):
        print(f"3D Vector: {self.x}x, {self.y}y, {self.z}z")

v2 = Vector2D(2, 4)
v2.show()

v3 = Vector3D(2, 4, 8)
v3.show()