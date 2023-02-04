from flask import Flask
from flask import json


app = Flask(__name__)


def get_products_list():
    with open('products.json') as f:
        return json.loads(f.read())


@app.route('/v1/products')
def index():
    data = get_products_list()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response
