from flask import url_for, render_template, flash, request
from flask import Blueprint
from stack_knowledge import app, db
from stack_knowledge.models.entries import Entry
from stack_knowledge.models.datasets_for_html import Datasets_For_Layout

entry = Blueprint('entry', __name__)

dataset_outcomes_layout = Datasets_For_Layout()
dataset_authors_layout  = Datasets_For_Layout()
dataset_subjects_layout = Datasets_For_Layout()

dataset_outcomes_layout.set_tables('outcomes', Entry.query.order_by(Entry.id.desc()).all())
dataset_outcomes_layout.set_tables('authors' , Entry.query.order_by(Entry.id.desc()).all())
dataset_outcomes_layout.set_tables('subjects', Entry.query.order_by(Entry.id.desc()).all())

@entry.route('/')
def show_stacks():
	hoge_entry_datas = Entry.query.order_by(Entry.id.desc()).all()
	return render_template('index.html', hoge_entry_datas = hoge_entry_datas, display_dict = dataset_outcomes_layout)

@entry.route('/entry/outcomes', methods = ['GET'])
def new_entry():
	return render_template('entry/outcomes.html', display_dict = dataset_outcomes_layout)

@entry.route('/display/outcomes', methods = ['GET'])
def display_outcomes():
	return render_template('display/outcomes.html', display_dict = dataset_outcomes_layout)

@entry.route('/display/authors', methods = ['GET'])
def display_authors():

	dataset_authors_layout.set_tables('authors', Entry.query.order_by(Entry.id.desc()).all())
	return render_template('display/authors.html', display_dict = dataset_authors_layout)

@entry.route('/display/subjects', methods = ['GET'])
def display_subjects():

	dataset_subjects_layout.set_tables('subjects', Entry.query.order_by(Entry.id.desc()).all())
	return render_template('display/subjects.html', display_dict = dataset_subjects_layout)

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
	return render_template('index.html', hoge_entry_datas = hoge_entry_datas, display_dict = dataset_outcomes_layout)
