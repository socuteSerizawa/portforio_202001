from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('development.cfg')

from stack_knowledge.views.entries import entry

app.register_blueprint(entry, url_prefix = '/')

from stack_knowledge.views import entries