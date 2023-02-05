from flask import abort, json, Flask, request
from werkzeug.exceptions import HTTPException


app = Flask(__name__)


def get_products_list():
    with open('products.json') as f:
        return json.loads(f.read())


@app.errorhandler(HTTPException)
def resource_not_found(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = e.get_response()
    response.data = json.dumps({
        'code': e.code,
        'name': e.name,
        'description': e.description,
    })
    response.content_type = 'application/json'
    return response


@app.route('/v1/products', methods=['GET'])
def list():
    args = request.args
    category = args.get('category')
    data = get_products_list()

    if category is not None:
        data = [p for p in data if p['category'] == category]

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/v1/products/<id>', methods=['GET'])
def get(id):
    # This check is made on purpose to simulate 400 error
    try:
        id = int(id)
    except ValueError:
        abort(400, description='Invalid product ID data type')
    
    data = get_products_list()
    for product in data:
        if product['id'] == id:
            response = app.response_class(
                response=json.dumps(product),
                status=200,
                mimetype='application/json'
            )
            return response

    abort(404, description='Product not found')
