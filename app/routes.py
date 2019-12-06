
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username':'Norie'}

    posts  = [

        {   'author':{'username':'John'},
            'title':'Portland visit',
            'body':'Beautiful day in Portland!'},
        {   'author':{'username':'Satan'},
            'title' :'Going to hell',
            'body':'Fine day in hell!'}
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)