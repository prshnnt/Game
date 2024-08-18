from .colors import *
import pygame

class BaseElement:
	def update(self):
		pass
	def show(self):
		pass
		
class Button(BaseElement):
	def __init__(self,size,center=(0,0),font_size=50):
		super().__init__()
		self.rect = pygame.Rect((center,size))
		self.bg = WHITE
		self.bg_hover = GRAY
		self.text = "Button"
		self.font = pygame.font.SysFont(pygame.font.get_default_font(),font_size)
		self.click = lambda : None

	def set_size(self,size):
		self.rect.w , self.rect.h = size

	def is_hover(self)->bool:
		return self.rect.collidepoint(pygame.mouse.get_pos())
	
	def is_click(self)->bool:
		return pygame.mouse.get_pressed()[0]
	def show(self,surface):
		if self.is_hover():
			if self.is_click():
				self.click()
				pygame.time.delay(100)
			pygame.draw.rect(surface,self.bg_hover,self.rect)
		else:
			pygame.draw.rect(surface,self.bg,self.rect)
		text = self.font.render(self.text,True,GREEN,(0,0,0,0))
		rect = text.get_rect()
		rect.center=self.rect.center
		surface.blit(text,rect)