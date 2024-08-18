import pygame
from core.screen import Environment , COLOR
from core.shapes import Circle , Rectangle ,Polygon ,Line
from core.page import Page
from core.components import BaseElement , Button
import numpy as np
import math
from random import randint , choice
pygame.init()
def percent_pos(length,percent):
    return length*percent/100

env = Environment((400,400),"black")
state = "start"
pages = {
    'start':Page(title="Start"),
    'menu':Page(title="Menu")
}
def set_state(name):
    global state
    if name in pages:
        env.EVENT.update(pages[name].get_handler())
        state= name
    else:
        raise KeyError("Invalid name")

pages['start'].elements.append(Button((200,100),center=(percent_pos(400,100)-200,percent_pos(400,0))))
pages['start'].elements.append(Button((200,100),center=(percent_pos(400,100)-200,percent_pos(400,10))))
0
pages['start'].elements[0].text = "Menu"
pages['start'].elements[0].click = lambda : set_state("menu")
pages['start'].elements[1].text = "Menu2"
pages['start'].elements[1].click = lambda : set_state("menu")
pages['start'].surface = env.SCREEN

pages['menu'].elements.append(Button((200,100)))
pages['menu'].elements[0].text = "start"
pages['menu'].elements[0].click = lambda : set_state("start")
pages['menu'].surface = env.SCREEN

def MOUSEBUTTONDOWN(self,event):
    self.touched = True

def MOUSEBUTTONUP(self,event):
    self.touched = False

def MOUSEMOTION(self,event):
    if self.touched:
        pass

env.EVENT[pygame.MOUSEBUTTONDOWN]=MOUSEBUTTONDOWN
env.EVENT[pygame.MOUSEBUTTONUP]=MOUSEBUTTONUP
env.EVENT[pygame.MOUSEMOTION]=MOUSEMOTION

def create(self):
    pass

def update(self):
    pages[state].render()

env.on("create",create)
env.on("update",update)
env.run()