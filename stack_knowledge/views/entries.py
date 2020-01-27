from flask import url_for, render_template, flash
from flask import Blueprint
from stack_knowledge import app

entry = Blueprint('entry', __name__)

@entry.route('/')
def show_stacks():
	return render_template('entries/index.html')