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

# Queries about artists
def selectArtists(name, surname, birthyearFrom, birthyearTo, artistType) :
    con = connection()

    cur = con.cursor()

    whereClause = " WHERE "

    fromClause = " FROM kalitexnis k "

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
        whereClause += " ETOS_GEN >= %d "
    if birthyearTo != None :
        if name != None or surname != None or birthyearFrom != None :
            whereClause += " AND "
        whereClause += " ETOS_GEN <= %d "

    # artistType = 1 --> singer
    # artistType = 2 --> song writer
    # artistType = 3 --> composer

    if artistType != None :
        if artistType == 1 :
            fromClause += " INNER JOIN singer_prod sp ON k.ar_taut = sp.tragoudistis "
        elif artistType == 2 : 
            fromClause += " INNER JOIN tragoudi tr ON k.ar_taut = tr.stixourgos "
        elif artistType == 3 : 
            fromClause += " INNER JOIN tragoudi tr ON k.ar_taut = tr.sinthetis "

    selectClause = " SELECT k.ar_taut, k.onoma, k.epitheto, k.etos_gen "

    parameters = []

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
        result = cur.fetchall()
        return result;
        con.close()

def updateArtist(id, name, surname, birthyear) :
    con = connection()

    cur = con.cursor()

    if id != None :
        updateQuery = " UPDATE kalitexnis SET "
    else :
        return

    if name != None :
        updateQuery += " ONOMA = '%s' "
    if surname != None :
        if name != None :
            updateQuery += " , "
        updateQuery += " EPITHETO = '%s' "
    if birthyear != None :
        if name != None or surname != None :
            updateQuery += " , "
        updateQuery += " ETOS_GEN = %d "

    updateQuery += " WHERE AR_TAUT = '%s' "

    parameters = [] 

    if name != None :
        parameters.append(name)
    if surname != None :
        parameters.append(surname)
    if birthyear != None :
        parameters.append(birthyear)
    if id != None :
        parameters.append(id)

    try:
        cur.execute(updateQuery, parameters)
    finally:
        con.commit()
        con.close()
        return [("STATUS"), ("OK")]    

def deleteArtist(id) :
    con = connection()

    cur = con.cursor()

    if id != None :
        deleteQuery = " DELETE FROM kalitexnis WHERE "
    else :
        return

    if id != None :
        deleteQuery += " AR_TAUT = '%s' "

    parameters = [] 

    if id != None :
        parameters.append(id)

    try:
        cur.execute(deleteQuery, parameters)
    finally:
        con.commit()
        con.close()
        return [("STATUS"), ("OK")]    

def insertArtist(id, name, surname, birthyear) :
    con = connection()

    cur = con.cursor()

    if id != None :
        insertQuery = " INSERT INTO kalitexnis (AR_TAUT, ONOMA, EPITHETO, ETOS_GEN) VALUES "
    else :
        return
    
    if id != None :
        insertQuery += " ( '%s' "
    if name != None :
        if id != None :
            insertQuery += " , "
        insertQuery += " ( '%s', "
    if surname != None :
        if id != None or name != None :
            insertQuery += " , "
        insertQuery += " '%s' "
    if birthyear != None :
        if id != None or name != None or surname != None :
            insertQuery += " , "
        insertQuery += " %d )"

    parameters = [] 

    if id != None :
        parameters.append(id)
    if name != None :
        parameters.append(name)
    if surname != None :
        parameters.append(surname)
    if birthyear != None :
        parameters.append(birthyear)

    try:
        cur.execute(insertQuery, parameters)
    finally:
        con.commit()
        con.close()
        return [("STATUS"), ("OK")]    

# Queries about songs
def selectSongs(title, composer, prodyear, songwriter) :
    con = connection()

    cur = con.cursor()

    whereClause = " WHERE "

    fromClause = " FROM tragoudi t "

    if title == None and composer == None and prodyear == None and songwriter == None :
        whereClause = ""

    if title != None :
        whereClause += " TITLOS = '%s' "
    if composer != None :
        if title != None :
            whereClause += " AND "
        whereClause += " SINTHETIS = '%s' "
    if prodyear != None :
        if title != None or composer != None :
            whereClause += " AND "
        whereClause += " ETOS_PAR = %d "
    if songwriter != None :
        if title != None or composer != None or songwriter != None :
            whereClause += " AND "
        whereClause += " STIXOURGOS = %s "
       
    selectClause = " SELECT t.titlos, t.sinthetis, t.etos_par, t.stixourgos "

    parameters = []

    if title != None :
        parameters.append(title)
    if composer != None :
        parameters.append(composer)
    if prodyear != None :
        parameters.append(prodyear)
    if songwriter != None :
        parameters.append(songwriter) 

    try:
        cur.execute(selectClause + fromClause + whereClause, (parameters))
    finally:
        result = cur.fetchall()
        return result
        con.close()

def updateSong(title, composer, prodyear, songwriter) :
    con = connection()

    cur = con.cursor()

    if title != None :
        updateQuery = " UPDATE tragoudi SET "
    else :
        return

    if composer != None :
        updateQuery += " SINTHETIS = '%s' "
    if prodyear != None :
        if composer != None :
            updateQuery += " , "
        updateQuery += " ETOS_PAR = '%s' "
    if songwriter != None :
        if composer != None or prodyear != None :
            updateQuery += " , "
        updateQuery += " STIXOURGOS = '%d' "

    updateQuery += " WHERE TITLOS = '%s' "

    parameters = [] 

    if composer != None :
        parameters.append(composer)
    if prodyear != None :
        parameters.append(prodyear)
    if songwriter != None :
        parameters.append(songwriter)
    if title != None :
        parameters.append(title)

    try:
        cur.execute(updateQuery, parameters)
    finally:
        con.commit()
        con.close()
        return [("STATUS"), ("OK")]    

def deleteSong(title) :
    con = connection()

    cur = con.cursor()

    if title != None :
        deleteQuery = " DELETE FROM tragoudi WHERE "
    else :
        return

    if title != None :
        deleteQuery += " TITLOS = '%s' "

    parameters = [] 

    if title != None :
        parameters.append(title)

    try:
        cur.execute(deleteQuery, parameters)
    finally:
        con.commit()
        con.close()
        return [("STATUS"), ("OK")]    

def insertSong(title, composer, prodyear, songwriter) :
    con = connection()

    cur = con.cursor()

    if title != None :
        insertQuery = " INSERT INTO tragoudi (TITLOS, SINTHETIS, ETOS_PAR, STIXOURGOS) VALUES "
    else :
        return
    
    if title != None :
        insertQuery += " ( '%s' "
    if composer != None :
        if title != None :
            insertQuery += " , "
        insertQuery += " ( '%s', "
    if prodyear != None :
        if title != None or composer != None :
            insertQuery += " , "
        insertQuery += " '%s' "
    if songwriter != None :
        if title != None or composer != None or prodyear != None :
            insertQuery += " , "
        insertQuery += " %d )"

    parameters = [] 

    if title != None :
        parameters.append(title)
    if composer != None :
        parameters.append(composer)
    if prodyear != None :
        parameters.append(prodyear)
    if songwriter != None :
        parameters.append(songwriter)

    try:
        cur.execute(insertQuery, parameters)
    finally:
        con.commit()
        con.close()
        return [("STATUS"), ("OK")] 