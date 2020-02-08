from stack_knowledge.static.layout_parameter import menu_contents
from stack_knowledge.static.layout_parameter import dropbox_cnt
from stack_knowledge.models.dropboxs import DropboxParts

class Datasets_For_Layout():

	def __init__(self):
		self.menu = []
		self.menu = menu_contents
		self.layout_state = self.menu[0]

	def set_state(self, state):
		self.layout_state = state

class Datasets_For_Display(Datasets_For_Layout):

	def __init__(self):
		super().__init__()
		self.display_dropbox = []
		self.table_menu = []
		self.dropbox_parts = {}

		self.table_date = []

	def set_parts(self, name, table_menu, display_dropbox):
		self.dropbox_parts[name] = DropboxParts(table_menu, self.organize_tables(display_dropbox))

	def organize_tables(self, tables):
		for i in range(dropbox_cnt - len(tables)):
			tables.append(None)
		return tables

	def set_state(self, state):
		super().set_state(state)
		res = self.dropbox_parts[self.layout_state]
		self.table_menu = res.table_menu
		self.display_dropbox = res.display_dropbox

