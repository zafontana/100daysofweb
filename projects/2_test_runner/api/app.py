import json
from typing import List

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
    suite_name = validators.String(max_length=50)
    suite_description = validators.String(max_length=300, allow_null=True)


# API methods

def list_suites() -> List[Suite]:
    return [Suite(suite[1]) for suite in sorted(suites.items())]



routes = [
    Route('/', method='GET', handler=list_suites),
    # Route('/', method='POST', handler=create_car),
    # Route('/{car_id}/', method='GET', handler=get_car),
    # Route('/{car_id}/', method='PUT', handler=update_car),
    # Route('/{car_id}/', method='DELETE', handler=delete_car),
]


app = App(routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)
