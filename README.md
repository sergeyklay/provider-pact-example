# Specmatic Testing Example

[![Check Contracts](https://github.com/sergeyklay/specmatic-testing-example/actions/workflows/contracts.yaml/badge.svg)](https://github.com/sergeyklay/specmatic-testing-example/actions/workflows/contracts.yaml)
[![Validate Action](https://github.com/sergeyklay/specmatic-testing-example/actions/workflows/versions.yaml/badge.svg)](https://github.com/sergeyklay/specmatic-testing-example/actions/workflows/versions.yaml)
[![Lint OpenAPI](https://github.com/sergeyklay/specmatic-testing-example/actions/workflows/lint.yaml/badge.svg)](https://github.com/sergeyklay/specmatic-testing-example/actions/workflows/lint.yaml)

## Requirements
- Python 3.8 >= 3.8
- Node.js >= 16

## How to try it out

### Install dependencies and tools

First, install Python dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Next, install Node.js linters and tools:
```bash
npm install
```

Finally, install [specmatic](https://specmatic.in/download/latest.html).

### Run API server

```bash
npm run server
```

### Run the contract tests

```bash
java -jar specmatic.jar test --testBaseURL=http://127.0.0.1:5000
```

### Run lint check

```bash
npm run lint
```

## Support

Should you have any question, any remark, or if you find a bug, or if there is something
you can't do with the Specmatic Testing Example, please
[open an issue](https://github.com/sergeyklay/specmatic-testing-example/issues).

## License

Specmatic Testing Example licensed under the MIT License.
See the [LICENSE](./LICENSE) file for more information.
