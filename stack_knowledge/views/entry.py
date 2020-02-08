from flask import url_for, render_template, flash, request, redirect
from stack_knowledge import app, db
from stack_knowledge.models.entries import *
from stack_knowledge.views.display import layout

# Create用メニューへ移行
@app.route('/entry', methods = ['POST'])
def select_entry():
	res = request.form['post_value']
	layout.set_state(res)

	return render_template('entry/create/'+ res +'.html', display_dict = layout)

# indexページへ移行
@app.route('/', methods = ['POST'])
def entry_outcomes():
	
	return redirect(url_for('entry.show_stacks')) 