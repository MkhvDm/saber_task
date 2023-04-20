from http import HTTPStatus
from typing import Tuple, Union

import yaml

from . import config as conf
from .exceptions import (BuildNameError, BuildsFileNotFound, EmptyBuildError,
                         TasksFileNotFound)


def get_data_from_files() -> Tuple[dict, dict]:
    """Загрузка файлов с билдами и задачами."""
    builds: dict = _prepare_builds_dict(conf.BUILDS_YAML_ABSPATH)
    tasks: dict = _prepare_tasks_dict(conf.TASKS_YAML_ABSPATH)
    return builds, tasks


def _prepare_tasks_dict(path: str) -> dict:
    """
    Загружаем файл tasks.yaml и преобразуем в словарь для быстрого поиска
    запрашиваемых task-ов.
    """
    result_tasks: dict = {}
    try:
        with open(path, 'r') as tasks_file:
            contents = tasks_file.read()
    except FileNotFoundError:
        raise TasksFileNotFound('Не найден файл с перечнем задач!')
    tasks: list = yaml.safe_load(contents).get('tasks')
    for task in tasks:
        if task.get('name') not in result_tasks.keys():
            result_tasks[task.get('name')] = task.get('dependencies')
    return result_tasks


def _prepare_builds_dict(path: str) -> dict:
    """
    Загружаем файл builds.yaml и преобразуем в словарь для быстрого поиска
    запрашиваемых build-ов.
    """
    result_builds: dict = {}
    try:
        with open(path, 'r') as builds_file:
            contents = builds_file.read()
    except FileNotFoundError:
        raise BuildsFileNotFound('Не найден файл с перечнем билдов!')
    builds: list = yaml.safe_load(contents).get('builds')
    for build in builds:
        if build.get('name') not in result_builds.keys():
            result_builds[build.get('name')] = build.get('tasks')
    return result_builds


def get_build_with_tasks(build_name: str, builds: dict) -> list:
    """Получить билд с тасками первого уровня вложенности."""
    try:
        print(builds[build_name])
        return builds[build_name]
    except KeyError:
        raise BuildNameError(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=f'Build name ({build_name}) not found in builds.yaml!'
        )


def get_tasks_with_dependencies(
        tasks: Union[list, None],
        tasks_dict: dict) -> list:
    """Получить список тасков с их зависимыми тасками."""
    result: list = []
    if tasks is None:
        raise EmptyBuildError(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Build has no tasks!'
        )
    for task in tasks:
        if task in tasks_dict.keys():
            result.append(task)
        dependencies = tasks_dict.get(task)
        if dependencies:
            result += get_tasks_with_dependencies(dependencies, tasks_dict)
    return result


def get_all_tasks(build_name: str, builds: dict, tasks: dict) -> list:
    """Получить для билда все таски, включая зависимые.
    Из-за рекурсивного обхода ограничение вложенности - 1000.
    """
    build_tasks: list = get_build_with_tasks(build_name, builds)
    all_tasks: list = get_tasks_with_dependencies(build_tasks, tasks)
    return all_tasks
