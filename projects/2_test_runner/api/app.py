import json
from typing import List

import ipdb
from apistar import App, Route, types, validators
from apistar.http import JSONResponse


# helpers

def _load_suites_data():
    with open('suites.json') as f:
        suites = json.loads(f.read())
        return {suite["id"]: suite for suite in suites}


suites = _load_suites_data()
# VALID_MANUFACTURERS = set([suite["manufacturer"]
#                            for suite in suites.values()])
SUITE_NOT_FOUND = 'Suite not found'


# definition

class Suite(types.Type):
    id = validators.Integer(allow_null=True)  # assign in POST
    suite_name = validators.String(max_length=50, allow_null=True)
    suite_description = validators.String(max_length=300, allow_null=True)


# API methods

def list_suites() -> List[Suite]:
    return [Suite(suite[1]) for suite in sorted(suites.items())]


def create_suite(suite: Suite) -> JSONResponse:
    suite_id = max(suites.keys()) + 1
    suite.id = suite_id
    suites[suite_id] = suite
    return JSONResponse(Suite(suite), status_code=201)


def get_suite(suite_id: int) -> JSONResponse:
    suite = suites.get(suite_id)
    if not suite:
        error = {"error": SUITE_NOT_FOUND}
        return JSONResponse(error, status_code=404)
    return JSONResponse(Suite(suite), status_code=200)


def update_suite(suite_id: int, suite:Suite) -> JSONResponse:
    if not suites.get(suite_id):
        error = {"error": SUITE_NOT_FOUND}
        return JSONResponse(error, status_code=404)

    suite.id = suite_id
    suites[suite_id] = suite
    return JSONResponse(Suite(suite), status_code=200)


def delete_suite(suite_id: int) -> JSONResponse:
    if not suites.get(suite_id):
        error = {"error": SUITE_NOT_FOUND}
        return JSONResponse(error, status_code=404)

    del suites[suite_id]
    return JSONResponse({}, status_code=204)


routes = [
    Route('/', method='GET', handler=list_suites),
    Route('/', method='POST', handler=create_suite),
    Route('/{suite_id}/', method='GET', handler=get_suite),
    Route('/{suite_id}/', method='PUT', handler=update_suite),
    Route('/{suite_id}/', method='DELETE', handler=delete_suite),
]


app = App(routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)

