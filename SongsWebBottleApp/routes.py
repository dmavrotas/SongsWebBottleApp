"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/artists')
@view('artistsselect')
def artistsselect():
    """Renders the update and search artists page."""
    return dict(
        title='Artists',
        message='Your update and search artists page.',
        year=datetime.now().year
    )

@route('/artistsview')
@view('artistsview')
def artistsview():
    """Renders the presentation of artists page."""
    return dict(
        title='Artists',
        message='Your update and search artists page.',
        year=datetime.now().year
    )

#@route('/contact')
#@view('contact')
#def contact():
#    """Renders the contact page."""
#    return dict(
#        title='Contact',
#        message='Your contact page.',
#        year=datetime.now().year
#    )

#@route('/about')
#@view('about')
#def about():
#    """Renders the about page."""
#    return dict(
#        title='About',
#        message='Your application description page.',
#        year=datetime.now().year
#    )
