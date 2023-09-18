from flask import Blueprint, request
from flask.views import MethodView

router = Blueprint('testRouter', __name__)

class Test(MethodView):

    def __init__(self) -> None:
        super().__init__()

    def get(self):
        return {'method': 'GET'}, 200
    
    def post(self):
        return {'method': 'POST'}, 200
    
    def patch(self):
        return {'method': 'PATCH'}, 200
    
    def delete(self):
        return {'method': 'DELETE'}, 200
    
router.add_url_rule('/', view_func=Test.as_view('test'))