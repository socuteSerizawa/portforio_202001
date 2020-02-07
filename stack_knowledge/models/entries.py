from stack_knowledge import db
from datetime import datetime

class Outcomes(db.Model):
	__tablename__ = 'outcomes'
	id = db.Column(db.Integer, primary_key = True)
	created_at = db.Column(db.DateTime)
	display_created_at = db.Column(db.String(50))
	stack_times = db.Column(db.Float)
	author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
	text = db.Column(db.String(50))

	related_outcomes_and_subjects_groups_id = db.relationship('RelatedOutcomesAndSubjectsGroups', backref = 'outcomes', lazy = True)

	def __init__(self, created_at = datetime.utcnow(), stack_times = None, author_id = None, text = None):
		self.created_at = created_at
		self.display_created_at = created_at.strftime('%Y-%m-%d %H:%M:%S')
		self.stack_times = stack_times
		self.author_id = author_id
		self.text = text

	def __repr__(self):
		return '<Entry id:{} created_at:{} display_created_at:{} stack_times:{} author_id:{} text:{}>'.format(self.id, self.created_at, self.display_created_at, self.stack_times, self.author_id, self.text)

class RelatedOutcomesAndSubjectsGroups(db.Model):
	__tablename__ = 'related_outcomes_and_subjects_group'
	id = db.Column(db.Integer, primary_key = True)
	outcomes_id = db.Column(db.Integer, db.ForeignKey('outcomes.id'))
	subjects_groups_id = db.Column(db.Integer, db.ForeignKey('subjects_groups.id'))

	def __init__(self, outcomes_id = None, subjects_groups_id = None):
		self.outcomes_id = outcomes_id
		self.subjects_groups_id = subjects_groups_id

	def __repr__(self):
		return '<Entry id:{} outcomes_id:{} subjects_groups_id:{}>'.format(self.id, self.outcomes_id, self.subjects_groups_id)

class SubjectsGroups(db.Model):
	__tablename__ = 'subjects_groups'
	id = db.Column(db.Integer, primary_key = True)
	group_name = db.Column(db.String(50))

	related_outcomes_and_subjects_groups_id = db.relationship('RelatedOutcomesAndSubjectsGroups', backref = 'subjects_groups', lazy = True)
	related_subjects = db.relationship('RelatedSubjectsAndGroups', backref = 'subjects_groups', lazy = True)

	def __init__(self, group_name = None):
		self.group_name = group_name

	def __repr__(self):
		return '<Entry id:{} name:{}>'.format(self.id, self.group_name)

class Authors(db.Model):
	__tablename__ = 'authors'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50))

	related_outcomes = db.relationship('Outcomes', backref = 'author', lazy = True)

	def __init__(self, name = None):
		self.name = name

	def __repr__(self):
		return '<Entry id:{} name:{}>'.format(self.id, self.name)

class Subjects(db.Model):
	__tablename__ = 'subjects'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50))

	related_subjects_and_groups = db.relationship('RelatedSubjectsAndGroups', backref = 'subjects', lazy = True)

	def __init__(self, name = None):
		self.name = name

	def __repr__(self):
		return '<Entry id:{} name:{}>'.format(self.id, self.name)

class RelatedSubjectsAndGroups(db.Model):
	__tablename__ = 'related_subject_and_groups'
	id = db.Column(db.Integer, primary_key = True)
	related_subjects_groups_id = db.Column(db.Integer, db.ForeignKey('subjects_groups.id'))
	related_subjects_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))

	def __init__(self, related_subjects_groups_id = None, related_subjects_id = None):
		self.related_subjects_groups_id = related_subjects_groups_id
		self.related_subjects_id = related_subjects_id

	def __repr__(self):
		return '<Entry id:{} related_subjects_groups_id:{} related_subjects_id:{}>'.format(self.id, self.related_subjects_groups_id, self.related_subjects_id)
