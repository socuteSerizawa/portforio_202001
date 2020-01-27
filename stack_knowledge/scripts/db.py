from flask_script import Command
from stack_knowledge import db

class InitDB(Command):
	"create database"

	def run(self):
		db.create_all()