import pygame as pg
from .shapes import Circle , Rectangle , Polygon ,Line
COLOR ={
    "black":(0,0,0),
    "white":(255,255,255),
    "red":(255,0,0),
    "green":(0,255,0),
    "blue":(0,0,255),
}

class  Environment:
    def __init__(self,window_size,background) -> None:
        (self.WIDTH,self.HEIGHT)=window_size
        self.BACKGROUND = background
        self.SCREEN = pg.display.set_mode(window_size)
        self.clock = pg.time.Clock()
        self.running =True
        self.touched = False
        self.state = "start"
        self.CALLBACK = {
            "update":lambda self : None,
            "create": lambda self : None ,
            "destroy":lambda self :None,
        }
        def quit_callback(self,event):
            self.running =False
        self.EVENT={pg.QUIT:quit_callback,}
    
    def on(self,name:str,callback):
        ### OPTIONS = ["create" ,"update","destroy"]
        self.CALLBACK[name]=callback

    def update(self):
        self.SCREEN.fill(COLOR[self.BACKGROUND])
        self.CALLBACK["update"](self)
        pg.display.update()

    def run(self):
        self.CALLBACK["create"](self)
        while self.running:
            for event in pg.event.get():
                try:
                    self.EVENT[event.type](self,event)
                except KeyError:
                    continue
                    
            self.update()
            self.clock.tick(60)

        self.CALLBACK["destroy"](self)
        pg.display.quit()
