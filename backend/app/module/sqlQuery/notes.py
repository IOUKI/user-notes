from app.module.sqlQuery.conn import doSqlStuff, selectSqlStuff

class NotesQuery:

    # add note
    @staticmethod
    def addNote(title, content):
        sqlQuery = f"INSERT INTO notes(Title, Content) \
                    VALUES ('{title}', '{content}');"
        doSqlStuff(sqlQuery)

    # select notes
    @staticmethod
    def selectNotes():
        sqlQuery = "SELECT ID, Title, Content \
                    FROM notes \
                    ORDER BY ID;"
        result = selectSqlStuff(sqlQuery)
        
        data = []
        for item in result:
            data.append({
                "ID": item[0],
                "Title": item[1],
                "Content": item[2]
            })
        
        return data
    
    # update note
    @staticmethod
    def updateNote(id, title, content):
        sqlQuery = f"UPDATE notes \
                    SET Title = '{title}', \
                        Content = '{content}' \
                    WHERE ID = {id};"
        doSqlStuff(sqlQuery)

    # delete note
    @staticmethod
    def deleteNote(id):
        sqlQuery = f"DELETE FROM notes WHERE ID = {id};"
        doSqlStuff(sqlQuery)