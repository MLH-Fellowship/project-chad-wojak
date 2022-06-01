import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    content = {
        'title': 'My Portfolio',
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
    return render_template('index.html', **content)
