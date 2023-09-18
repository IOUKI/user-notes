from flask import Blueprint, request, jsonify
from flask.views import MethodView
from app.module.sqlQuery.notes import NotesQuery

router = Blueprint('notesRouter', __name__)

class NewAndSelectNotes(MethodView):

    def __init__(self) -> None:
        super().__init__()

    # select notes
    def get(self):
        data = NotesQuery.selectNotes()
        return data, 200

    # add note
    def post(self):
        try:
            title = request.get_json()['title']
            content = request.get_json()['content']

            NotesQuery.addNote(title, content)

            return '', 201
        
        except Exception as e:
            print(e)
            return '', 404
    
class UpdateAndDeleteNotes(MethodView):

    def __init__(self) -> None:
        super().__init__()

    # update note
    def patch(self, id):
        try:
            print(id)
            title = request.get_json()['title']
            content = request.get_json()['content']
            NotesQuery.updateNote(id, title, content)

            return '', 204
        
        except Exception as e:
            print(e)
            return '', 404
    
    # delete note
    def delete(self, id):
        try:
            NotesQuery.deleteNote(id)
            return '', 204
        except Exception as e:
            print(e)
            return '', 404

router.add_url_rule('/', view_func=NewAndSelectNotes.as_view('NewAndSelectNotes'))
router.add_url_rule('/<int:id>', view_func=UpdateAndDeleteNotes.as_view('UpdateAndDeleteNotes'))
