import json

from aiohttp.web import Request, Response
from tinydb import TinyDB, Query

from validators import ValidatorSequence

def consists_of(obj: dict, source: dict):
    if len(obj) - 1 > len(source):
        return False
    return all([(key == 'name' or source.get(key) == obj[key]) for key in obj])

async def get_form(request: Request) -> Response:
    validator_sequence: ValidatorSequence = request.app["validator_sequence"]
    db: TinyDB = request.app["db"]

    params = await request.post()

    params = {key: validator_sequence.get_type(params[key]) for key in params}

    template_name = None
    max_fields = 0
    for template in db.search(Query().map(lambda x: x).test(consists_of, params)):
        if len(template) > max_fields:
            template_name = template["name"]
            max_fields = len(template)

    if not template_name:
        return Response(status=404, content_type='application/json', body=json.dumps(params))
    
    return Response(status=200, content_type='application/json', body=json.dumps(template_name))