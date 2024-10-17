import math

class Rectangle:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def square_of_intersection_with(self, rect):
        left = max(self.x, rect.x)
        right = min(self.x + self.width, rect.x + rect.width)
        top = min(self.y + self.height, rect.y + rect.height)
        bottom = max(self.y, rect.y)

        width = right - left
        height = top - bottom

        if (width < 0 or height < 0):
            return 0

        return width * height

    @staticmethod
    def square_of_intersection_beetwen(rect1, rect2):
        left = max(rect1.x, rect2.x)
        right = min(rect1.x + rect1.width, rect2.x + rect2.width)
        top = min(rect1.y + rect1.height, rect2.y + rect2.height)
        bottom = max(rect1.y, rect2.y)

        width = right - left
        height = top - bottom

        if (width < 0 or height < 0):
            return 0

        return width * height


#rect = Rectangle(10, 10, 5, 5)
#rect2 = Rectangle(5, 5, 7, 7)
#print(Rectangle.square_of_intersection_beetwen(rect, rect2))

class Circle:

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def square_of_intersection_with(self, circle):
        distance = math.sqrt((self.x - circle.x) ** 2 + (self.y - circle.y) ** 2)

        if distance >= self.radius + circle.radius:
            return 0

        if distance <= abs(self.radius - circle.radius):
            return min(self.radius ** 2,
                       circle.radius ** 2) * math.pi

        r1 = self.radius
        r2 = circle.radius
        a = 2 * math.acos((r1 ** 2 + distance ** 2 - r2 ** 2) / (2 * r1 * distance))
        b = 2 * math.acos((r2 ** 2 + distance ** 2 - r1 ** 2) / (2 * r2 * distance))
        square = 0.5 * (r1 ** 2 * (a - math.sin(a)) + r2 ** 2 * (b - math.sin(b)))
        return square

    @staticmethod
    def square_of_intersection_beetwen(circle1, circle2):
        distance = math.sqrt((circle1.x - circle2.x) ** 2 + (circle1.y - circle2.y) ** 2)

        if distance >= circle1.radius + circle2.radius:
            return 0

        if distance <= abs(circle1.radius - circle2.radius):
            return min(circle1.radius ** 2,
                       circle2.radius ** 2) * math.pi

        r1 = circle1.radius
        r2 = circle2.radius
        a = 2 * math.acos((r1 ** 2 + distance ** 2 - r2 ** 2) / (2 * r1 * distance))
        b = 2 * math.acos((r2 ** 2 + distance ** 2 - r1 ** 2) / (2 * r2 * distance))
        square = 0.5 * (r1 ** 2 * (a - math.sin(a)) + r2 ** 2 * (b - math.sin(b)))
        return square

#circle1 = Circle(0, 0, 2)
#circle2 = Circle(3, 0, 4)
#print(circle1.square_of_intersection_with(circle2))
#print(Circle.square_of_intersection_beetwen(circle1, circle2))
