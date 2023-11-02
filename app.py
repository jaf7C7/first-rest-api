from flask import Flask, request
from db import stores
import uuid

app = Flask(__name__)


@app.get('/')
def index():
    return {
        'endpoints': [
            {'endpoint': '/echo', 'description': 'Echoes POSTed JSON back to the sender'},
            {'endpoint': '/stores', 'description': 'Returns data on all stores'}
        ]
    }, 200

@app.post('/echo')
def echo():
    return request.get_json(), 200


@app.get('/stores')
def get_all_stores():
    return {'stores': list(stores.values())}, 200


@app.post('/stores')
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    new_store = {'id': store_id, **store_data}
    stores[store_id] = new_store
    return new_store, 201
