"""
This file contains the database interaction logic of the application.
"""

import pymysql as db
import settings

def connection() : 
    con = db.connect(
        settings.mysql_host,
        settings.mysql_user,
        settings.mysql_passwd,
        settings.mysql_schema)
    return con

def selectArtists(name, surname, birthyearFrom, birthyearTo, artistType) :
    con = connection()

    cur = con.cursor()

    whereClause = " WHERE "

    fromClause = " FROM %s.kalitexnis k "

    if name == None and surname == None and birthyearFrom == None and birthyearTo == None and artistType == None : 
        whereClause = ""

    if name != None :
        whereClause += " ONOMA = '%s' "
    if surname != None :
        if name != None :
            whereClause += " AND "
        whereClause += " EPITHETO = '%s' "
    if birthyearFrom != None :
        if name != None or surname != None :
            whereClause += " AND "
        whereClause += " ETOS_GEN >= TO_DATE('%s', 'DD-MM-YYYY') "
    if birthyearTo != None :
        if name != None or surname != None or birthyearFrom != None :
            whereClause += " AND "
        whereClause += " ETOS_GEN <= TO_DATE('%s', 'DD-MM-YYYY') "

    # artistType = 1 --> singer
    # artistType = 2 --> song writer
    # artistType = 3 --> composer

    if artistType != None :
        if artistType == 1 :
            fromClause += " INNER JOIN %s.singer_prod sp ON k.ar_taut = sp.tragoudistis "
        elif artistType == 2 : 
            fromClause += " INNER JOIN %s.tragoudi tr ON k.ar_taut = tr.stixourgos "
        elif artistType == 3 : 
            fromClause += " INNER JOIN %s.tragoudi tr ON k.ar_taut = tr.sinthetis "

    selectClause = " SELECT k.ar_taut, k.onoma, k.epitheto, k.etos_gen "

    parameters = [ settings.mysql_schema ]

    if name != None :
        parameters.append(name)
    if surname != None :
        parameters.append(surname)
    if birthyearFrom != None :
        parameters.append(birthyearFrom)
    if birthyearTo != None :
        parameters.append(birthyearTo)

    try :
        cur.execute(selectClause + fromClause + whereClause, (parameters))
    finally :
        return cur.fetchall()
        con.close()

def selectSongs() :


        


