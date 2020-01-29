from flask import url_for, render_template, flash, request
from flask import Blueprint
from stack_knowledge import app, db
from stack_knowledge.models.entries import Entry

entry = Blueprint('entry', __name__)

@entry.route('/')
def show_stacks():
	hoge_entry_datas = Entry.query.order_by(Entry.id.desc()).all()
	return render_template('display/index.html', hoge_entry_datas = hoge_entry_datas)

@entry.route('/display/outcomes', methods = ['GET'])
def new_entry():
	return render_template('entry/outcomes.html')

@entry.route('/display/outcomes', methods = ['GET'])
def display_outcomes():
	return render_template('display/outcomes.html')

@entry.route('/display/authors', methods = ['GET'])
def display_authors():
	return render_template('display/authors.html')

@entry.route('/display/subjects', methods = ['GET'])
def display_subjects():
	return render_template('display/subjects.html')

@entry.route('/display/outcomes', methods = ['POST'])
def entry_outcomes():

	hoge_entry = Entry(
		title = request.form['title'],
		text  = request.form['text']
		)
	db.session.add(hoge_entry)
	db.session.commit()
	db.session.close()

	hoge_entry_datas = Entry.query.order_by(Entry.id.desc()).all()
	return render_template('display/index.html', hoge_entry_datas = hoge_entry_datas)
