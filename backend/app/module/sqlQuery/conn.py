from mysql import connector
from app.config.config import SqlUser

# get mysql connect
def getConn():
    return connector.connect(
        host=SqlUser.host,
        user=SqlUser.user,
        password=SqlUser.password,
        database=SqlUser.database
    )

# insert, update, delete DB
def doSqlStuff(sqlQuery):
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute(sqlQuery)
    conn.commit()
    conn.close()

# select DB
def selectSqlStuff(sqlQuery):
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute(sqlQuery)
    result = cursor.fetchall()
    conn.close()
    return result