# How to run tests
We're calling pytest through `pytest -m pytest`. This allows us to add `services` to `sys.path`. Note that the dependencies should be installed in `services` before running the tests, otherwise you may get `ModuleNotFoundError` error messages. See information about this [here](https://docs.pytest.org/en/stable/how-to/usage.html#calling-pytest-through-python-m-pytest).

## Run all tests
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
