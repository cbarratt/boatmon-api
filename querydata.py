from flask import g

def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv

def get_temperatures():
    obj = {
        'temperatures': []
    }

    for data in query_db('SELECT channel_name AS name, round(channel_data, 3) AS value FROM data WHERE channel_id IN (0,1,2,3)'):
        obj['temperatures'].append(data)

    return obj

def get_voltages():
    obj = {
        'voltages': []
    }

    for data in query_db('SELECT channel_name AS name, round(channel_data, 3) AS value FROM data WHERE channel_id IN (4,5,6,7,8,9,10)'):
        obj['voltages'].append(data)

    return obj
