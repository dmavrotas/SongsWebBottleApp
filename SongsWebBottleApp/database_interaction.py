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
        settings.mysql_schema,
        charset='utf8')
    return con

# Queries about artists
def selectArtists(name, surname, birthyearFrom, birthyearTo, artistType) :
    con = connection()

    cur = con.cursor()

    whereClause = " WHERE "

    fromClause = " FROM kalitexnis k "
    
    if not name and not surname and not birthyearFrom and not birthyearTo : 
        whereClause = ''

    if name :
        whereClause += " ONOMA = %s "
    if surname :
        if name :
            whereClause += " AND "
        whereClause += " EPITHETO = %s "
    if birthyearFrom :
        if name  or surname :
            whereClause += " AND "
        whereClause += " ETOS_GEN >= CAST(%s AS UNSIGNED) "
    if birthyearTo :
        if name or surname or birthyearFrom :
            whereClause += " AND "
        whereClause += " ETOS_GEN <= CAST(%s AS UNSIGNED) "

    # artistType = 1 --> singer
    # artistType = 2 --> song writer
    # artistType = 3 --> composer

    if artistType :
        if artistType == '1' :
            fromClause += " INNER JOIN singer_prod sp ON k.ar_taut = sp.tragoudistis "
        elif artistType == '2' : 
            fromClause += " INNER JOIN tragoudi tr ON k.ar_taut = tr.stixourgos "
        elif artistType == '3' : 
            fromClause += " INNER JOIN tragoudi tr ON k.ar_taut = tr.sinthetis "

    selectClause = " SELECT DISTINCT k.ar_taut, k.onoma, k.epitheto, k.etos_gen "

    parameters = []

    if name :
        parameters.append(name)
    if surname :
        parameters.append(surname)
    if birthyearFrom :
        parameters.append(birthyearFrom)
    if birthyearTo :
        parameters.append(birthyearTo)

    try :
        cur.execute(selectClause + fromClause + whereClause.strip(), (parameters))
    finally :
        result = cur.fetchall()
        return result;
        con.close()

def updateArtist(id, name, surname, birthyear) :
    con = connection()

    cur = con.cursor()

    if id :
        updateQuery = " UPDATE kalitexnis SET "
    else :
        return

    if name :
        updateQuery += " ONOMA = %s "
    if surname :
        if name :
            updateQuery += " , "
        updateQuery += " EPITHETO = %s "
    if birthyear :
        if name or surname :
            updateQuery += " , "
        updateQuery += " ETOS_GEN = CAST(%s AS UNSIGNED) "

    updateQuery += " WHERE AR_TAUT = %s "

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

    if id :
        deleteQuery = " DELETE FROM kalitexnis WHERE "
    else :
        return

    if id :
        deleteQuery += " AR_TAUT = %s "

    parameters = [] 

    if id :
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

    if id :
        insertQuery = " INSERT INTO kalitexnis (AR_TAUT, ONOMA, EPITHETO, ETOS_GEN) VALUES "
    else :
        return
    
    if id :
        insertQuery += " ( %s "
    if name :
        if id :
            insertQuery += " , "
        insertQuery += " ( %s, "
    if surname :
        if id or name :
            insertQuery += " , "
        insertQuery += " %s "
    if birthyear :
        if id or name or surname :
            insertQuery += " , "
        insertQuery += " CAST(%s AS UNSIGNED) )"

    parameters = [] 

    if id :
        parameters.append(id)
    if name :
        parameters.append(name)
    if surname :
        parameters.append(surname)
    if birthyear :
        parameters.append(birthyear)

    try:
        cur.execute(insertQuery, parameters)
    finally:
        con.commit()
        con.close()
        return [("STATUS"), ("OK")]    

# Queries about songs
def selectSongs(title, company, prodyear) :
    con = connection()

    cur = con.cursor()

    whereClause = " WHERE "

    fromClause = " FROM tragoudi T "

    if not title and not company and not prodyear :
        whereClause = ""

    if title :
        whereClause += " T.TITLOS = %s "
    if company :
        if title :
            whereClause += " AND "
        whereClause += " CD.ETAIREIA = %s "
    if prodyear :
        if title or company :
            whereClause += " AND "
        whereClause += " T.ETOS_PAR = CAST(%s AS UNSIGNED) "

    fromClause += " INNER JOIN SINGER_PROD S ON T.TITLOS = S.TITLE INNER JOIN CD_PRODUCTION CD ON S.CD = CD.CODE_CD "
       
    selectClause = " SELECT DISTINCT t.titlos, t.sinthetis, t.stixourgos, t.etos_par, cd.etaireia "

    parameters = []

    if title :
        parameters.append(title)
    if company :
        parameters.append(company)
    if prodyear :
        parameters.append(prodyear) 

    try:
        cur.execute(selectClause + fromClause + whereClause, (parameters))
    finally:
        result = cur.fetchall()
        return result
        con.close()

def updateSong(title, composer, prodyear, songwriter) :
    con = connection()

    cur = con.cursor()

    if title :
        updateQuery = " UPDATE tragoudi SET "
    else :
        return

    if composer :
        updateQuery += " SINTHETIS = %s "
    if prodyear :
        if composer :
            updateQuery += " , "
        updateQuery += " ETOS_PAR = CAST(%s AS UNSIGNED) "
    if songwriter :
        if composer or prodyear :
            updateQuery += " , "
        updateQuery += " %s "

    updateQuery += " WHERE TITLOS = %s "

    parameters = [] 

    if composer :
        parameters.append(composer)
    if prodyear :
        parameters.append(prodyear)
    if songwriter :
        parameters.append(songwriter)
    if title :
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

    if title :
        deleteQuery = " DELETE FROM tragoudi WHERE "
    else :
        return

    if title :
        deleteQuery += " TITLOS = %s "

    parameters = [] 

    if title :
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

    if title :
        insertQuery = " INSERT INTO tragoudi (TITLOS, SINTHETIS, ETOS_PAR, STIXOURGOS) VALUES "
    else :
        return
    
    if title :
        insertQuery += " ( %s "
    if composer :
        if title :
            insertQuery += " , "
        insertQuery += " ( %s, "
    if prodyear :
        if title or composer :
            insertQuery += " , "
        insertQuery += " CAST(%s AS UNSIGNED) "
    if songwriter :
        if title or composer or prodyear :
            insertQuery += " , "
        insertQuery += " %s )"

    parameters = [] 

    if title :
        parameters.append(title)
    if composer :
        parameters.append(composer)
    if prodyear :
        parameters.append(prodyear)
    if songwriter :
        parameters.append(songwriter)

    try:
        cur.execute(insertQuery, parameters)
    finally:
        con.commit()
        con.close()
        return [("STATUS"), ("OK")] 