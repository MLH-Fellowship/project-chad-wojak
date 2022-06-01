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
        }]
}

@app.route('/')
def index():
    content = {
        'title': 'Home - Portfolio',
        'active_tab': '',
        **base_content
    }
    return render_template('index.html', **content)

@app.route('/about')
def about():
    content = {
        'title': 'About - Portfolio',
        'active_tab': 'about',
        **base_content
    }
    return render_template('about.html', **content)

@app.route('/education')
def education():
    content = {
        'title': 'Education - Portfolio',
        'active_tab': 'education',
        **base_content
    }
    return render_template('education.html', **content)

@app.route('/hobbies')
def hobbies():
    content = {
        'title': 'Hobbies - Portfolio',
        'active_tab': 'hobbies',
        **base_content
    }
    return render_template('hobbies.html', **content)

@app.route('/where-am-i')
def where_am_i():
    content = {
        'title': 'Where am I - Portfolio',
        'active_tab': 'where-am-i',
        **base_content
    }
    return render_template('where-am-i.html', **content)