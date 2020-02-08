from flask import url_for, render_template, flash, request
from stack_knowledge import app, db
from stack_knowledge.views import layout

@app.route('/')
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

	list0 = []
	if layout.layout_state == layout.menu[0]:
		layout.table_menu = ['更新時間', 'グループ名', '勉強時間', '編集者', '詳細']
		layout.table_date = db.session.query(Outcomes.display_created_at, SubjectsGroups.group_name, Outcomes.stack_times, Authors.name, Outcomes.text, RelatedOutcomesAndSubjectsGroups).join(SubjectsGroups).join(Outcomes).join(Authors).order_by(Outcomes.display_created_at.desc()).all()
		layout.table_date = except_last_idx(layout.table_date)
		list0.append([layout.menu[0], db.session.query(Outcomes.id, Outcomes.display_created_at).order_by(Outcomes.id.asc()).all()])
		list0.append([layout.menu[1], db.session.query(Authors.id, Authors.name).order_by(Authors.id.asc()).all()])
		list0.append([layout.menu[2], db.session.query(SubjectsGroups.id, SubjectsGroups.group_name).order_by(SubjectsGroups.id.asc()).all()])
		list0.append([layout.menu[3], db.session.query(Subjects.id, Subjects.name).order_by(Subjects.id.asc()).all()])

	elif layout.layout_state == layout.menu[1]:
		layout.table_menu = ['編集者']
		layout.table_date = db.session.query(Authors.name).order_by(Authors.id.desc()).all()

	elif layout.layout_state == layout.menu[2]:
		layout.table_menu = ['グループ名', '登録科目']
		layout.table_date = db.session.query(SubjectsGroups.group_name, Subjects.name, RelatedSubjectsAndGroups).join(SubjectsGroups).join(Subjects).order_by(Subjects.id.desc()).all()
		layout.table_date = except_last_idx(layout.table_date)
		list0.append([layout.menu[2], db.session.query(SubjectsGroups.id, SubjectsGroups.group_name).order_by(SubjectsGroups.id.asc()).all()])
		list0.append([layout.menu[3], db.session.query(Subjects.id, Subjects.name).order_by(Subjects.id.asc()).all()])
		
	elif layout.layout_state == layout.menu[3]:
		layout.table_menu = ['登録科目']
		layout.table_date = db.session.query(Subjects.name).order_by(Subjects.id.desc()).all()

	layout.set_tables(list0)

	return render_template('index.html', display_dict = layout)