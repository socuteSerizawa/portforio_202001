from flask import url_for, render_template, flash, request, redirect
from stack_knowledge import app, db
from stack_knowledge.models.entries import *
from stack_knowledge.views.display import layout

# Create用メニューへ移行
@app.route('/entry', methods = ['POST'])
def select_entry():

	# ディクショナリに「表の項目名」，「ドロップボックス情報」を収納
	table_menu = ['Authors', 'SubjectsGroups'] # Only Englsh!!!
	list0 = []
	list0.append([layout.menu[1], db.session.query(Authors.id, Authors.name).order_by(Authors.id.asc()).all()])
	list0.append([layout.menu[2], db.session.query(SubjectsGroups.id, SubjectsGroups.group_name).order_by(SubjectsGroups.id.asc()).all()])
	layout.set_parts(layout.menu[0], table_menu, list0)

	table_menu = ['subject'] # Only Englsh!!!
	list0 = []
	list0.append([layout.menu[3], db.session.query(Subjects.id, Subjects.name).order_by(Subjects.id.asc()).all()])
	layout.set_parts(layout.menu[2], table_menu, list0)

	res = request.form['post_value']
	layout.set_state(res)
		
	return render_template('entry/create/'+ res +'.html', display_dict = layout)

# indexページへ移行
@app.route('/', methods = ['POST'])
def entry_outcomes():
	res = request.form
	if   layout.layout_state == layout.menu[0]:
		# Outcomesを新規作成
		outcomes_data = Outcomes(stack_times  = res["OutcomeTime"], author_id = res[layout.table_menu[0]], text = res["OutcomesText"])
		db.session.add(outcomes_data)
		db.session.commit()

		# 追加したOutcomesIDにSubjectGroupsIDを紐付け
		# 追加したOutcomesIDを取得
		created_outcomes_id = db.session.query(Outcomes.id).count()
		# POSTから受け取ったSubjectGroupsIDをlist化し，整列（重複成分は削除）
		create_group_id_list = []
		for selected_id in range(1, 3 + 1):
			res_id = res[layout.table_menu[1] + '_' + str(selected_id)]
			if res_id != 'None':
				create_group_id_list.append(int(res_id))
		# DBに登録
		for order_by_selected_id in set(create_group_id_list):
			related_outcomes_subjects_group_data = RelatedOutcomesAndSubjectsGroups(outcomes_id = created_outcomes_id, subjects_groups_id  = order_by_selected_id)
			db.session.add(related_outcomes_subjects_group_data)
		db.session.commit()

	elif layout.layout_state == layout.menu[1]:
		author_data = Authors(name = res["author_name"])
		db.session.add(author_data)
		db.session.commit()

	elif layout.layout_state == layout.menu[2]:
		# SubjectGroupsを新規作成
		subjects_group_data = SubjectsGroups(group_name = res["Subject_Group_name"])
		db.session.add(subjects_group_data)
		db.session.commit()

		# 追加したSubjectGroupsIDにsubjectIDを紐付け
		# 追加したSubjectGroupsIDを取得
		created_group_id = db.session.query(SubjectsGroups.id).count()
		# POSTから受け取ったsubjectIDをlist化し，整列（重複成分は削除）
		create_subject_id_list = []
		for selected_id in range(1, 3 + 1):
			res_id = res[layout.table_menu[0] + '_' + str(selected_id)]
			if res_id != 'None':
				create_subject_id_list.append(int(res_id))
		# DBに登録
		for order_by_selected_id in set(create_subject_id_list):
			related_subjects_group_data = RelatedSubjectsAndGroups(related_subjects_groups_id = created_group_id, related_subjects_id  = order_by_selected_id)
			db.session.add(related_subjects_group_data)
		db.session.commit()
		
	elif layout.layout_state == layout.menu[3]:
		subject_data = Subjects(name = res["Subject_name"])
		db.session.add(subject_data)
		db.session.commit()

	
	return redirect(url_for('entry.show_stacks')) 