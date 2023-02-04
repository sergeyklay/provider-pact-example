from flask import abort, json, Flask


app = Flask(__name__)


def get_products_list():
    with open('products.json') as f:
        return json.loads(f.read())


@app.errorhandler(404)
def resource_not_found(e):
    response = e.get_response()
    response.data = json.dumps({
        'code': e.code,
        'name': e.name,
        'description': e.description,
    })
    response.content_type = 'application/json'
    return response


@app.route('/v1/products', methods=['GET'])
def index():
    data = get_products_list()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/v1/products/<int:id>', methods=['GET'])
def get(id):
    data = get_products_list()
    for product in data:
        if product['id'] == id:
            response = app.response_class(
                response=json.dumps(product),
                status=200,
                mimetype='application/json'
            )
            return response

    abort(404, description="Resource not found")
