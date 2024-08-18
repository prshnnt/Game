class Page:
	def __init__(self,title="Page"):
		self.elements = []
		self.title = title
		self.handler = {}
		self.surface = None

	def render(self):
		for element in self.elements:
			element.update()
			element.show(self.surface)
	def get_handler(self):
		return self.handler