from http import HTTPStatus

from .exceptions import JSONKeyError, JSONValueError


def validate_request_dict(input_dict: dict):
    if 'build' not in input_dict.keys():
        raise JSONKeyError(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Invalid JSON key! Expected key: "build".'
        )
    if not isinstance(input_dict['build'], str):
        raise JSONValueError(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Invalid JSON value! Must be a string.'
        )
    return True
