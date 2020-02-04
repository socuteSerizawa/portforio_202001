from stack_knowledge.static.layout_parameter import menu_contents as parameters

class Datasets_For_Layout():

	menu = []
	layout_state = None

	def __init__(self):
		self.menu = []
		self.menu = parameters
		self.layout_state = self.menu[0]

	def set_state(self, state):
		self.layout_state = state

class Datasets_For_Display(Datasets_For_Layout):

	display_dropbox = {}

	def __init__(self):
		super().__init__()
		self.display_dropbox = {}

	def set_tables(self, name, tables):
		self.display_dropbox[name] = tables

