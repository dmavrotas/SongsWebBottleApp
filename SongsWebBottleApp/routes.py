"""
Routes and views for the bottle application.
"""

from bottle import route, view, request, app, template
from datetime import datetime
import database_interaction as db

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/artists', method=['GET'])
@view('artistsselect')
def artistsselect():
    if request.GET.get('submitNew','').strip():
        result = db.selectArtists(request.GET.get('name').strip(), request.GET.get('surname').strip(), request.GET.get('byfrom').strip(), request.GET.get('byto').strip(), request.GET.get('artisttype').strip())
        output = template('artistsview', rows=result)
        return output
    else:
        return template('artistsselect')

@route('/artistsview')
@view('artistsview')
def artistsview():
    return template('artistsview')
