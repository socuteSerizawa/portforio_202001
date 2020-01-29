from flask import url_for, render_template, flash, request
from flask import Blueprint
from stack_knowledge import app, db
from stack_knowledge.models.entries import Entry

entry = Blueprint('entry', __name__)

@entry.route('/')
def show_stacks():
	hoge_entry_datas = Entry.query.order_by(Entry.id.desc()).all()
	return render_template('entry/index.html', hoge_entry_datas = hoge_entry_datas)

@entry.route('/entry/outcomes', methods = ['GET'])
def new_entry():
	return render_template('entry/outcomes.html')

@entry.route('/entry/outcomes', methods = ['POST'])
def entry_outcomes():

	hoge_entry = Entry(
		title = request.form['title'],
		text  = request.form['text']
		)
	db.session.add(hoge_entry)
	db.session.commit()
	db.session.close()

	hoge_entry_datas = Entry.query.order_by(Entry.id.desc()).all()
	return render_template('entry/index.html', hoge_entry_datas = hoge_entry_datas)
