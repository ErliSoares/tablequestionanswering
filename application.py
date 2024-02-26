from flask import Flask, request

from app.tapex import execute_query


def create_app():
    app = Flask(__name__)

    @app.route('/ai/question', methods=['POST'])
    def question():
        req_json = request.get_json()
        return execute_query(req_json['question'], req_json['data'])

    return app
