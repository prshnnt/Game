import pygame
class Shape:
    def __init__(self,center=(0,0)):
        self.center = center
        self.relative = None
        self.color = (255,255,255)
    def relative_to(self,shape):
        self.relative = shape
    def get_center(self):
        if self.relative is not None:
            rel_center = self.relative.get_center()
            return (self.center[0]+rel_center[0],self.center[1]+rel_center[1])
        else:
            return self.center

    def update(self):
        pass

    def draw(self,surface,*args,**kwargs):
        pass

class Circle(Shape):
    def __init__(self,radius=1,center=(0,0)):
        super().__init__(center)
        self.radius = radius
        self.border = 0
    def draw(self,surface,*args,**kwargs):
        pygame.draw.circle(surface,self.color,self.get_center(),self.radius,width=self.border,*args,**kwargs)

class Rectangle(Shape):
    def __init__(self,center=(0,0),size =(10,10)):
        super().__init__(center)
        self.rect = pygame.Rect(((0,0),size))
        self.rect.center = self.get_center()
        self.border = 0
    def update(self):
        self.rect.center = self.get_center()

    def draw(self,surface,*args,**kwargs):
        pygame.draw.rect(surface,self.color,self.rect,width=self.border,*args,**kwargs)

class Polygon(Shape):
    def __init__(self,center=(0,0)):
        super().__init__(center)
        self.points = []
        self.border = 0
    def add_point(self,point):
        self.points.append(point)
    def remove_point(self,index):
        self.points.pop(index)

    def update(self):
        c = self.get_center()
        for i in range(len(self.points)):
            self.points[i][0] = c[0]
            self.points[i][1] = c[1]
    def draw(self,surface,*args,**kwargs):
        pygame.draw.polygon(surface,self.color,self.points,width=self.border,*args,**kwargs)


class Line:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.width = 1
    def draw(self,surface,*args,**kwargs):
        pygame.draw.line(surface,self.color,self.start,self.end ,width=self.width, *args,**kwargs)