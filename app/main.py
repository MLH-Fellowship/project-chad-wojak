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

hobby_content = {
    'hobbies': [{
            'name': 'Badminton',
            'img': 'https://cdn.shopify.com/s/files/1/0020/9407/1890/files/2_480x480.jpg?v=1559302854',
            'desc': 'II l]]]]ove badmintonI l]]]]ove badmintonI l]]]]ove badmintonI l]]]]ove badmintonI l]]]]ove badmintonI l]]]]ove badmintonI l]]]]ove badmintonI l]]]]ove badminton l]]]]ove badminton'
        },
        {
            'name': 'Chess',
            'img': 'https://www.chess.com/bundles/web/images/offline-play/standardboard.1d6f9426.png',
            'desc': 'I I love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhlove ches ches cheshh'
        },
        {
            'name': 'Chess',
            'img': 'https://www.chess.com/bundles/web/images/offline-play/standardboard.1d6f9426.png',
            'desc': 'I I love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhlove ches ches cheshh'
        },
        {
            'name': 'Chess',
            'img': 'https://www.chess.com/bundles/web/images/offline-play/standardboard.1d6f9426.png',
            'desc': 'I I love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhlove ches ches cheshh'
        }
    ]
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
        'hobbies': [
                       {
                           'name': 'Badminton',
                           'img': 'https://cdn.shopify.com/s/files/1/0020/9407/1890/files/2_480x480.jpg?v=1559302854',
                           'desc': 'II l]]]]ove badmintonI l]]]]ove badmintonI l]]]]ove badmintonI l]]]]ove badmintonI l]]]]ove badmintonI l]]]]ove badmintonI l]]]]ove badmintonI l]]]]ove badminton l]]]]ove badminton'
                       },
                       {
                           'name': 'Chess',
                           'img': 'https://www.chess.com/bundles/web/images/offline-play/standardboard.1d6f9426.png',
                           'desc': 'I I love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhlove ches ches cheshh'
                       },
                       {
                           'name': 'Chess',
                           'img': 'https://www.chess.com/bundles/web/images/offline-play/standardboard.1d6f9426.png',
                           'desc': 'I I love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhlove ches ches cheshh'
                       },
                       {
                           'name': 'Chess',
                           'img': 'https://www.chess.com/bundles/web/images/offline-play/standardboard.1d6f9426.png',
                           'desc': 'I I love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhI love ches ches cheshhlove ches ches cheshh'
                       }
                   ],
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


if __name__ == "__main__":
    app.run()