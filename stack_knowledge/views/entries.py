from flask import url_for, render_template, flash, request
from flask import Blueprint
from stack_knowledge import app, db
from stack_knowledge.models.entries import *
from stack_knowledge.models.datasets_for_html import Datasets_For_Layout

entry = Blueprint('entry', __name__)

dataset_outcomes_layout = Datasets_For_Layout()
dataset_authors_layout  = Datasets_For_Layout()
dataset_subjects_layout = Datasets_For_Layout()

@entry.route('/')
def show_stacks():
	'''
	hoge_entry = Author(
		name = 'Taroooo'
		)
	db.session.add(hoge_entry)
	db.session.commit()

	hoge_entry = Subjects(
		name = 'math'
		)
	db.session.add(hoge_entry)
	hoge_entry = Subjects(
		name = 'science'
		)
	db.session.add(hoge_entry)
	db.session.commit()

	hoge_entry = Outcomes(
		overwrite_at = datetime.utcnow(),
		times  = 1,
		author_id = 1,
		text = 'testd'
		)
	db.session.add(hoge_entry)
	db.session.commit()

	hoge_entry = OutcomesRelated(
		outcomes_id = 1,
		subject_related_id  = 1,
		)
	db.session.add(hoge_entry)
	hoge_entry = OutcomesRelated(
		outcomes_id = 1,
		subject_related_id  = 2,
		)
	db.session.add(hoge_entry)
	db.session.commit()
	'''

	dataset_outcomes_layout.set_tables('outcomes', Outcomes.query.order_by(Outcomes.id.desc()).all())
	dataset_outcomes_layout.set_tables('authors' , Author.query.order_by(Author.id.desc()).all())
	dataset_outcomes_layout.set_tables('subjects', Subjects.query.order_by(Subjects.id.desc()).all())

	hoge_entry_datas = Outcomes.query.order_by(Outcomes.id.desc()).all()

	# users = db.session.query(Outcomes, Author).join(Author).all()
	# users : list
	# users[0] = (result:'Outcomes', result:'Author') : tupple
	# users[0][0] = <class 'stack_knowledge.models.entries.Outcomes'>
	# But 'print(users[0][0])' display __repr__()

	# subject = db.session.query(OutcomesRelated, Subjects, Outcomes).join(Outcomes).join(Subjects).all()
	# db.session.query(OutcomesRelated, Subjects, Outcomes) : outer join

	return render_template('index.html', hoge_entry_datas = hoge_entry_datas, display_dict = dataset_outcomes_layout)

@entry.route('/entry/outcomes', methods = ['GET'])
def new_entry():
	return render_template('entry/outcomes.html', display_dict = dataset_outcomes_layout)

@entry.route('/display/outcomes', methods = ['GET'])
def display_outcomes():
	return render_template('display/outcomes.html', display_dict = dataset_outcomes_layout)

@entry.route('/display/authors', methods = ['GET'])
def display_authors():

	dataset_authors_layout.set_tables('authors', Outcomes.query.order_by(Outcomes.id.desc()).all())
	return render_template('display/authors.html', display_dict = dataset_authors_layout)

@entry.route('/display/subjects', methods = ['GET'])
def display_subjects():

	dataset_subjects_layout.set_tables('subjects', Outcomes.query.order_by(Outcomes.id.desc()).all())
	return render_template('display/subjects.html', display_dict = dataset_subjects_layout)

@entry.route('/', methods = ['POST'])
def entry_outcomes():

	return render_template('index.html', hoge_entry_datas = hoge_entry_datas, display_dict = dataset_outcomes_layout)
