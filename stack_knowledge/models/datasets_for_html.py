from stack_knowledge.static.layout_parameter import menu_contents
from stack_knowledge.static.layout_parameter import dropbox_cnt

class Datasets_For_Layout():

	menu = []
	layout_state = None

	def __init__(self):
		self.menu = []
		self.menu = menu_contents
		self.layout_state = self.menu[0]

	def set_state(self, state):
		self.layout_state = state

class Datasets_For_Display(Datasets_For_Layout):

	display_dropbox = []
	table_menu = []
	table_date = []

	def __init__(self):
		super().__init__()
		self.display_dropbox = []
		self.table_menu = []
		self.table_date = []

	def set_tables(self, tables):
		self.display_dropbox = tables
		for i in range(dropbox_cnt - len(tables)):
			self.display_dropbox.append(None)

