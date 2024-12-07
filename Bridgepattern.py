#Bride pattern seperates an object abstraction from its implementation allowing the two to evovle independently
class DrawingAPI1:
    def draw_circle(self,x,y,radius):
        print(f"Api1.circle at ({x},{y})with radius{radius}")
class DrawingAPI2:
    def draw_circle(self,x,y,radius):
        print(f"API2.circle at({x},{y})with radius{radius}")
class circle:
    def __init__(self,x,y,radius,drawing_api):
        self.x=x
        self.y=y
        self.radius=radius
        self.drawing_api=drawing_api
    def draw(self):
        self.drawing_api.draw_circle(self.x,self.y,self.radius)

circle1=circle(1,2,3,DrawingAPI1())
circle2=circle(5,7,9,DrawingAPI2())
circle1.draw()
circle2.draw()