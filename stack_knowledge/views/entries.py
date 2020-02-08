from flask import url_for, render_template, flash, request
from flask import Blueprint
from stack_knowledge import app, db
from stack_knowledge.models.entries import *
from stack_knowledge.models.datasets_for_html import Datasets_For_Display
from stack_knowledge.models.dropboxs import DropboxParts

# from flask_script import Manager
# from sqlalchemy.dialects import mysql

entry = Blueprint('entry', __name__)

layout = Datasets_For_Display()
'''
@entry.route('/entry', methods = ['POST'])
def new_entry():
	# res = request.args.get('get_value')
	# print(res)
	return render_template('entry/outcomes.html', display_dict = layout)
'''

@entry.route('/')
def show_stacks():
	'''
	hoge_entry = Authors(
		name = 'Taroooo'
		)
	db.session.add(hoge_entry)
	hoge_entry = Authors(
		name = 'John'
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
		stack_times  = 1,
		author_id = 1,
		text = 'testd'
		)
	db.session.add(hoge_entry)
	db.session.commit()
	hoge_entry = Outcomes(
		stack_times  = 34,
		author_id = 2,
		text = 'testdwefewfw'
		)
	db.session.add(hoge_entry)
	db.session.commit()

	hoge_entry = RelatedOutcomesAndSubjectsGroups(
		outcomes_id = 1,
		subjects_groups_id  = 1,
		)
	db.session.add(hoge_entry)
	hoge_entry = RelatedOutcomesAndSubjectsGroups(
		outcomes_id = 1,
		subjects_groups_id  = 2,
		)
	db.session.add(hoge_entry)
	db.session.commit()
	
	hoge_entry = SubjectsGroups(
		group_name = 'Python',
		)
	db.session.add(hoge_entry)
	hoge_entry = SubjectsGroups(
		group_name = 'Math',
		)
	db.session.add(hoge_entry)
	db.session.commit()
	
	hoge_entry = RelatedSubjectsAndGroups(
		related_subjects_groups_id = 1,
		related_subjects_id  = 1,
		)
	db.session.add(hoge_entry)
	hoge_entry = RelatedSubjectsAndGroups(
		related_subjects_groups_id = 1,
		related_subjects_id  = 2,
		)
	db.session.add(hoge_entry)
	db.session.commit()
	'''
	
	# users = db.session.query(Outcomes, Author).join(Author).all()
	# users : list
	# users[0] = (result:'Outcomes', result:'Author') : tupple
	# users[0][0] = <class 'stack_knowledge.models.entries.Outcomes'>
	# But 'print(users[0][0])' display __repr__()

	# subject = db.session.query(OutcomesRelated, Subjects, Outcomes).join(Outcomes).join(Subjects).all()
	# db.session.query(OutcomesRelated, Subjects, Outcomes) : outer join

	# subject = db.session.query(OutcomesRelated, Subjects, Outcomes).join(Outcomes).join(Subjects)
	# varify sql query
	# print(subject.statement.compile(dialect=mysql.dialect(), compile_kwargs={"literal_binds": True}))
	'''
	query = db.session.query(Outcomes.overwrite_at, SubjectsGroups.group_name, Outcomes.stack_times, Outcomes.text, RelatedOutcomesAndSubjectsGroups).join(SubjectsGroups).join(Outcomes)
	print()
	print(query.statement.compile(dialect=mysql.dialect(), compile_kwargs={"literal_binds": True}))
	list0 = query.all()
	for i in list0[-1]:
		print(type(i))
	print()
	'''

	
	table_menu = ['更新時間', 'グループ名', '勉強時間', '編集者', '詳細']
	list0 = []
	list0.append([layout.menu[0], db.session.query(Outcomes.id, Outcomes.display_created_at).order_by(Outcomes.id.asc()).all()])
	list0.append([layout.menu[1], db.session.query(Authors.id, Authors.name).order_by(Authors.id.asc()).all()])
	list0.append([layout.menu[2], db.session.query(SubjectsGroups.id, SubjectsGroups.group_name).order_by(SubjectsGroups.id.asc()).all()])
	list0.append([layout.menu[3], db.session.query(Subjects.id, Subjects.name).order_by(Subjects.id.asc()).all()])
	layout.set_parts(layout.menu[0], table_menu, list0)

	table_menu = ['編集者']
	list0 = []
	layout.set_parts(layout.menu[1], table_menu, list0)

	table_menu = ['グループ名', '登録科目']
	list0 = []
	list0.append([layout.menu[2], db.session.query(SubjectsGroups.id, SubjectsGroups.group_name).order_by(SubjectsGroups.id.asc()).all()])
	list0.append([layout.menu[3], db.session.query(Subjects.id, Subjects.name).order_by(Subjects.id.asc()).all()])
	layout.set_parts(layout.menu[2], table_menu, list0)

	table_menu = ['登録科目']
	list0 = []
	layout.set_parts(layout.menu[3], table_menu, list0)


	layout.table_date = db.session.query(Outcomes.display_created_at, SubjectsGroups.group_name, Outcomes.stack_times, Authors.name, Outcomes.text, RelatedOutcomesAndSubjectsGroups).join(SubjectsGroups).join(Outcomes).join(Authors).order_by(Outcomes.display_created_at.desc()).all()
	layout.table_date = except_last_idx(layout.table_date)


	return render_template('index.html', display_dict = layout)
	
@entry.route('/entry', methods = ['POST'])
def select_entry():
	res = request.form['post_value']
	layout.set_state(res)

	return render_template('entry/create/'+ res +'.html', display_dict = layout)

@entry.route('/display', methods = ['POST'])
def select_display():
	res = request.form['post_value']
	layout.set_state(res)
	if   layout.layout_state == layout.menu[0]:
		layout.table_date = db.session.query(Outcomes.display_created_at, SubjectsGroups.group_name, Outcomes.stack_times, Authors.name, Outcomes.text, RelatedOutcomesAndSubjectsGroups).join(SubjectsGroups).join(Outcomes).join(Authors).order_by(Outcomes.display_created_at.desc()).all()
		layout.table_date = except_last_idx(layout.table_date)

	elif layout.layout_state == layout.menu[1]:
		layout.table_date = db.session.query(Authors.name).order_by(Authors.id.desc()).all()

	elif layout.layout_state == layout.menu[2]:
		layout.table_date = db.session.query(SubjectsGroups.group_name, Subjects.name, RelatedSubjectsAndGroups).join(SubjectsGroups).join(Subjects).order_by(Subjects.id.desc()).all()
		layout.table_date = except_last_idx(layout.table_date)
		
	elif layout.layout_state == layout.menu[3]:
		layout.table_date = db.session.query(Subjects.name).order_by(Subjects.id.desc()).all()

	return render_template('display/'+ res +'.html', display_dict = layout)

def except_last_idx(target_list):
	for idx in range(len(target_list)):
		target_list[idx] = target_list[idx][:-1]
	return target_list

@entry.route('/display/detail/', methods = ['POST'])
def select_data():
	res = request.form

	if layout.layout_state == layout.menu[0]:
		query = db.session.query(Outcomes.display_created_at, SubjectsGroups.group_name, Outcomes.stack_times, Authors.name, Outcomes.text, RelatedOutcomesAndSubjectsGroups).join(SubjectsGroups).join(Outcomes).join(Authors).order_by(Outcomes.display_created_at.desc())
		if res[layout.menu[0]] != 'None':
			query = query.filter(Outcomes.id == int(res[layout.menu[0]]))
		if res[layout.menu[1]] != 'None':
			query = query.filter(Authors.id == int(res[layout.menu[1]]))
		if res[layout.menu[2]] != 'None':
			query = query.filter(SubjectsGroups.id == int(res[layout.menu[2]]))
		if res[layout.menu[3]] != 'None':
			query = query.filter(Subjects.id == int(res[layout.menu[3]]))
		layout.table_date = query.all()
		layout.table_date = except_last_idx(layout.table_date)
	if layout.layout_state == layout.menu[2]:
		query = db.session.query(SubjectsGroups.group_name, Subjects.name, RelatedSubjectsAndGroups).join(SubjectsGroups).join(Subjects).order_by(Subjects.id.desc())
		if res[layout.menu[2]] != 'None':
			query = query.filter(SubjectsGroups.id == int(res[layout.menu[2]]))
		if res[layout.menu[3]] != 'None':
			query = query.filter(Subjects.id == int(res[layout.menu[3]]))
		layout.table_date = query.all()
		layout.table_date = except_last_idx(layout.table_date)

	return render_template('display/'+ layout.layout_state +'.html', display_dict = layout)

'''
@entry.route('/', methods = ['POST'])
def entry_outcomes():

	return render_template('index.html', hoge_entry_datas = hoge_entry_datas, display_dict = layout)
'''
