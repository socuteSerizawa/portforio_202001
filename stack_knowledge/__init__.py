from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('development.cfg')

from stack_knowledge.views import entries