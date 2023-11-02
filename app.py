from flask import Flask, request

app = Flask(__name__)


@app.get('/')
def index():
    return {
        'endpoints': [
            {'endpoint': '/echo', 'description': 'Echoes POSTed JSON back to the sender'}
        ]
    }, 200

@app.post('/echo')
def echo():
    return request.get_json(), 200
