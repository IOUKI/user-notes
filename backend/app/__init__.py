from flask import Flask
from flask_cors import CORS

def createApp(debug=True):
    app = Flask(__name__)
    app.debug = debug

    CORS(app)

    from app.module.apiRoute.test import router as testRouter
    from app.module.apiRoute.notes import router as notesRouter
    app.register_blueprint(testRouter, url_prefix='/api/test')
    app.register_blueprint(notesRouter, url_prefix='/api/notes')

    return app