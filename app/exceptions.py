from fastapi import HTTPException


class JSONPostRequestError(HTTPException):
    pass


class JSONKeyError(HTTPException):
    pass


class JSONValueError(HTTPException):
    pass


class BuildNameError(HTTPException):
    pass


class EmptyBuildError(HTTPException):
    pass


class BuildsFileNotFound(Exception):
    pass


class TasksFileNotFound(Exception):
    pass
