#!/usr/bin/env python
import os
import urllib
import json
import random
from flask import Flask
from flask import render_template
from forms import SearchForm

app = Flask(__name__)
app.secret_key = 'some_secret_key'

# custom jinja line delimeters
app.jinja_env.line_statement_prefix = '%'
app.jinja_env.line_comment_prefix = '##'

@app.route("/", methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        query = form.query.data
    # returning an html template
    return render_template('index.html', form=form)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', debug=True, port=port)
