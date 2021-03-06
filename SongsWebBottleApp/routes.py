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
    return template('index')

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
    if request.GET.get('edit','').strip():
        result = db.selectArtistByID(request.GET.get('edit').strip())
        name = ''
        surname = ''
        byear = ''
        for res in result:
            name = res[0]
            surname = res[1]
            byear = res[2]
        return template('updateartist', id=request.GET.get('edit').strip(), name = name, surname = surname, byear = byear)

@route('/insertartist', method=['GET'])
@view('insertartist')
def insertartist():
    if request.GET.get('submitNew','').strip():
        result = db.insertArtist(request.GET.get('natid').strip(), request.GET.get('name').strip(), request.GET.get('surname').strip(), request.GET.get('byear').strip())
        return template('insertartist')
    else:
        return template('insertartist')

@route('/updateartist', method=['GET'])
@view('updateartist')
def insertartist():
    if request.GET.get('submitNew','').strip():
        result = db.updateArtist(request.GET.get('submitNew').strip(), request.GET.get('name').strip(), request.GET.get('surname').strip(), request.GET.get('byear').strip())
        return template('updateartist', id = '', name = '', surname = '', byear = '')

@route('/songs', method=['GET'])
@view('songsselect')
def songsselect():
    if request.GET.get('submitNew','').strip():
        result = db.selectSongs(request.GET.get('title').strip(), request.GET.get('company').strip(), request.GET.get('prodyear').strip())
        output = template('songsview', rows=result)
        return output
    else:
        return template('songsselect')

@route('/songsview')
@view('songsview')
def songsview():
    return template('songsview')

@route('/insertsong')
@view('insertsong')
def insertsong():
    if request.GET.get('submitNew','').strip():
        result = db.insertSong(request.GET.get('title').strip(), request.GET.get('composer').strip(), request.GET.get('prodyear').strip(), request.GET.get('songwriter').strip(), request.GET.get('cd').strip(), request.GET.get('singer').strip())
        cdsongs = db.getSongsCDs()
        singers = db.getSongsSingers()
        composers = db.getSongComposers()
        songwriters = db.getSongsSongWriters()
        return template('insertsong', cds = cdsongs, cdsingers = singers, cdcomposers = composers, cdsongwriters = songwriters)
    else:
        cdsongs = db.getSongsCDs()
        singers = db.getSongsSingers()
        composers = db.getSongComposers()
        songwriters = db.getSongsSongWriters()
        return template('insertsong', cds = cdsongs, cdsingers = singers, cdcomposers = composers, cdsongwriters = songwriters)
