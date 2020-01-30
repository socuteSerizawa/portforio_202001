from stack_knowledge import db
from datetime import datetime

class Outcomes(db.Model):
	__tablename__ = 'outcomes'
	id = db.Column(db.Integer, primary_key = True)
	created_at = db.Column(db.DateTime)
	overwrite_at = db.Column(db.DateTime)
	times = db.Column(db.Float)
	author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
	text = db.Column(db.String(50))

	outcomes_related = db.relationship('OutcomesRelated', backref = 'outcome', lazy = True)

	def __init__(self, overwrite_at = None, times = None, author_id = None, text = None):
		self.created_at = datetime.utcnow()
		self.overwrite_at = overwrite_at
		self.times = times
		self.author_id = author_id
		self.text = text

	def __repr__(self):
		return '<Entry id:{} created_at:{} overwrite_at:{} times:{} author_id:{} text:{}>'.format(self.id, self.created_at, self.overwrite_at, self.times, self.author_id, self.text)

class OutcomesRelated(db.Model):
	__tablename__ = 'outcomes_related'
	id = db.Column(db.Integer, primary_key = True)
	outcomes_id = db.Column(db.Integer, db.ForeignKey('outcomes.id'))
	subject_related_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))

	def __init__(self, outcomes_id = None, subject_related_id = None):
		self.outcomes_id = outcomes_id
		self.subject_related_id = subject_related_id

	def __repr__(self):
		return '<Entry id:{} outcomes_id:{} subject_related_id:{}>'.format(self.id, self.outcomes_id, self.subject_related_id)

class Author(db.Model):
	__tablename__ = 'authors'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50))

	outcomes = db.relationship('Outcomes', backref = 'author', lazy = True)

	def __init__(self, name = None):
		self.name = name

	def __repr__(self):
		return '<Entry id:{} name:{}>'.format(self.id, self.name)

class Subjects(db.Model):
	__tablename__ = 'subjects'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50))

	subjects_related = db.relationship('SubjectsRelated', backref = 'subjects', lazy = True)
	outcomes_related = db.relationship('OutcomesRelated', backref = 'subjects', lazy = True)

	def __init__(self, name = None):
		self.name = name

	def __repr__(self):
		return '<Entry id:{} name:{}>'.format(self.id, self.name)

class SubjectsRelated(db.Model):
	__tablename__ = 'subjects_related'
	id = db.Column(db.Integer, primary_key = True)
	#subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))
	related_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))

	def __init__(self, subject_id = None, related_id = None):
		#self.subject_id = subject_id
		self.related_id = related_id

	def __repr__(self):
		return '<Entry id:{} related_id:{}>'.format(self.id, self.related_id)
