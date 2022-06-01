import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
@app.route("/home")
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

@app.route("/about")
def about_me():
     content = {
         'name': 'Insert Your Name here'
         ''
     }
    return render_template('about.html', **content)

if __name__ == '__main__':
    app.run(debug=True)
