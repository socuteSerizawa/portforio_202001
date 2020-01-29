from stack_knowledge.static.layout_parameter import menu_contents as parameters

class Datasets_For_Layout():

	menu = {}
	display_dropbox = {}

	def __init__(self):
		self.menu = parameters

	def set_tables(self, name, tables):
		self.display_dropbox[name] = tables