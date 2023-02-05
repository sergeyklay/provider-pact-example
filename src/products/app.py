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
    data = get_products_list()
    args = request.args

    category = args.get('category')
    q = args.get('q')
    
    products = []
    for p in data:
        if q is not None and len(q.strip()) > 0:
            descr = p['description'].lower()
            title = p['title'].lower()
            brand = p['brand'].lower()
            if q.lower() not in descr and q.lower() not in title and q.lower() not in brand:
                continue
        if category is not None and len(category.strip()) > 0:
            if p['category'].lower() != category.lower():
                continue
        products.append(p)

    response = app.response_class(
        response=json.dumps(products),
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
