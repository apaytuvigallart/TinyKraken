# How to run tests
Execute tests using `pytest` via the command:

```sh
pytest -m pytest
```

This approach ensures that the services directory is included in `sys.path`, allowing for proper module resolution during test execution. Ensure that all dependencies within services are installed prior to running tests; otherwise, Python may raise `ModuleNotFoundError` exceptions.

For detailed guidance on invoking pytest through Python and managing `sys.path`, refer to the official documentation [here](https://docs.pytest.org/en/stable/how-to/usage.html#calling-pytest-through-python-m-pytest).

## Run all tests
```sh
cd services
python -m pytest 
```

## Run all tests from a specific service
```sh
cd services
python -m pytest api/tests
```

## Run tests from a specific file
```sh
cd services
python -m pytest api/tests/test_api.py
```

## Run a specific test from a specific file
```sh
cd services
python -m pytest api/tests/test_api.py::test_list_comments
```
