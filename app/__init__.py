import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


base_content = {
        'name': 'MLH Fellow',
        'position': 'Software Engineer',
        'url': os.getenv("URL"),
        'socials': [{
            'name': 'Github',
            'url': 'https://github.com/MLH-Fellowship',
            'icon': './static/img/social/github.svg'
        }, {
            'name': 'LinkedIn',
            'url': 'https://www.linkedin.com/company/major-league-hacking/',
            'icon': './static/img/social/linkedin.svg'
        }],
        # Whether it is an initial page load, and we should play the page load animations
        'initial': True,
}

@app.route('/')
def index():
    content = {
        **base_content,
        'title': 'Home - Portfolio',
        'active_tab': 'home'
    }
    return render_template('index.html', **content)

@app.route('/about')
def about():
    content = {
        **base_content,
        'title': 'About - Portfolio',
        'active_tab': 'about'
    }
    from_page = request.args.get('from')
    if from_page is not None:
        content = {
            **content,
            'initial': False
        }
    return render_template('about.html', **content)

@app.route('/education')
def education():
    content = {
        **base_content,
        'title': 'Education - Portfolio',
        'active_tab': 'education'
    }
    from_page = request.args.get('from')
    if from_page is not None:
        content = {
            **content,
            'initial': False
        }
    return render_template('education.html', **content)

@app.route('/hobbies')
def hobbies():
    content = {
        **base_content,
        'title': 'Hobbies - Portfolio',
        'active_tab': 'hobbies'
    }
    from_page = request.args.get('from')
    if from_page is not None:
        content = {
            **content,
            'initial': False
        }
    return render_template('hobbies.html', **content)

@app.route('/where-am-i')
def where_am_i():
    content = {
        **base_content,
        'title': 'Where am I - Portfolio',
        'active_tab': 'where-am-i',
        'places': [{
            'name': 'San Francisco',
            'description': 'I am currently living in San Francisco, California (lie)',
            'coords': [37.75, -122.4]
        },{
            'name': 'Edmonton',
            'description': 'Capital of the texas of canada',
            'coords': [53, -113]
        }]
    }
    from_page = request.args.get('from')
    if from_page is not None:
        content = {
            **content,
            'initial': False
        }
    return render_template('where-am-i.html', **content)
