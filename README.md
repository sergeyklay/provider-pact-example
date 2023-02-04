# Specmatic Testing Example

## How to try it out

### Install project dependencies

First, install python dependencies:ß

```bash
python3 -m pip install -r requirements.txt
```

Next, install [specmatic](https://specmatic.in/download/latest.html).

### Run products API server

```bash
cd src/products
flask run &
```

### Run the tests

```bash
java -jar specmatic.jar test --testBaseURL=http://127.0.0.1:5000
```

## License

Specmatic Testing Example licensed under the MIT License.
See the [LICENSE](./LICENSE) file for more information.
