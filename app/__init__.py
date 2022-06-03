import os
from flask import Flask, make_response, render_template, request
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
    resp = make_response(render_template('index.html', **content))
    resp.set_cookie('prev_page', 'home')
    return resp

@app.route('/about')
def about():
    content = {
        **base_content,
        'title': 'About - Portfolio',
        'active_tab': 'about'
    }
    prev_page = request.cookies.get('prev_page', None, type=str)
    print(f'prev_page for about: {prev_page}')
    if prev_page is not None and prev_page != 'about':
        content = {
            **content,
            'initial': False
        }
    resp = make_response(render_template('about.html', **content))
    resp.set_cookie('prev_page', 'about')
    return resp


@app.route('/education')
def education():
    content = {
        **base_content,
        'title': 'Education - Portfolio',
        'active_tab': 'education'
    }
    prev_page = request.cookies.get('prev_page', None, type=str)
    print(f'prev_page for education: {prev_page}')
    if prev_page is not None and prev_page != 'education':
        content = {
            **content,
            'initial': False
        }
    resp = make_response(render_template('education.html', **content))
    resp.set_cookie('prev_page', 'education')
    return resp 

@app.route('/hobbies')
def hobbies():
    content = {
        **base_content,
        'title': 'Hobbies - Portfolio',
        'active_tab': 'hobbies'
    }
    prev_page = request.cookies.get('prev_page', None, type=str)
    print(f'prev_page for hobbies: {prev_page}')
    if prev_page is not None and prev_page != 'hobbies':
        content = {
            **content,
            'initial': False
        }
    resp = make_response(render_template('hobbies.html', **content))
    resp.set_cookie('prev_page', 'hobbies')
    return resp

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
    prev_page = request.cookies.get('prev_page', None, type=str)
    print(f'prev_page for where-am-i: {prev_page}')
    if prev_page is not None and prev_page != 'where-am-i':
        content = {
            **content,
            'initial': False
        }
    resp = make_response(render_template('where-am-i.html', **content))
    resp.set_cookie('prev_page', 'where-am-i')
    return resp
