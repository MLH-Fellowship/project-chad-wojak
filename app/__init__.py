import os
from typing import Any
from flask import Flask, make_response, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Base content all pages need
# used by the "profile" section of the template
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
    # no extra content needed
    # title and active_tab handled by `handle_route`
    return handle_route('Home', 'index', base_content)


@app.route('/about')
def about():
    content = {
        **base_content,
        'quote': 'Only one who devotes himself to a cause with his whole strength and soul can be a true master. For this reason mastery demands all of a person.',
        'author': 'Albert Einstein',
    }
    return handle_route('About', 'about', content)


@app.route('/education')
def education():
    content = {
        **base_content,
    }
    return handle_route('Education', 'education', content)


@app.route('/hobbies')
def hobbies():
    content = {
        **base_content,
    }
    return handle_route('Hobbies', 'hobbies', content)


@app.route('/where-am-i')
def where_am_i():
    content = {
        **base_content,
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
    return handle_route('Where am I', 'where-am-i', content)


def handle_route(name: str, id: str, content: dict[str, Any]):
    '''
    Handles routing logic for each page

    Args:
        name: Page name (Shows in the navbar)
        id: unique id for the page
        content: extra content to pass to the template
    '''
    content = {
        **content,
        'title': f'{name} - Portfolio',
        'active_tab': id,
    }
    # check prev_page cookie to see what animations we have to do
    prev_page = request.cookies.get('prev_page', None, type=str)
    print(f'prev_page for {id}: {prev_page}')
    if prev_page is None or prev_page == id:
        # This is an initial page load (user first navigates, or refreshes)
        # `initial` is used by the template to know to play the fadein animations
        content = {
            **content,
            'initial': True,
        }
    else:
        # This is not an initial page load, so set a slide animation for the content
        content = {
            **content,
            'initial': False,
            'content_slide_animation': get_animation(prev_page, id)
        }
    # set the prev_page cookie to the `id`, 
    # so the next link will know what page transition to do
    resp = make_response(render_template(f'{id}.html', **content))
    resp.set_cookie('prev_page', id)
    return resp


# from the two pages, gets the animate.css animation to play
# either a `animate__slideInLeft` or `animate__slideInRight`
def get_animation(prev_page: str, curr_page: str) -> str:
    pages = {'index': 0, 'about': 1, 'education': 2, 'hobbies': 3, 'where-am-i': 4}
    anim = 'slideInRight' if pages[prev_page] < pages[curr_page] else 'slideInLeft'
    return f'animate__{anim}'


if __name__ == '__main__':
    app.run(debug=True)
