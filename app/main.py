from http import HTTPStatus
from json import JSONDecodeError

from fastapi import FastAPI, Request

from .exceptions import JSONPostRequestError
from .utils import get_all_tasks, get_data_from_files
from .validators import validate_request_dict

app = FastAPI()
BUILDS, TASKS = get_data_from_files()


@app.post('/get_tasks')
async def get_tasks(request: Request):
    try:
        req_json = await request.json()
    except JSONDecodeError:
        raise JSONPostRequestError(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Invalid JSON!'
        )
    if validate_request_dict(req_json):
        build_name = req_json['build']
        tasks = get_all_tasks(build_name, BUILDS, TASKS)
    return tasks
