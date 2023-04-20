from fastapi.testclient import TestClient

from .main import app


def test_valid_request():
    request_data = {"build": "test_build"}
    with TestClient(app) as client:
        response = client.post(
            "/get_tasks",
            json=request_data
        )
    assert response.status_code == 200
    assert response.json() == [
        "bring_gray_fairies",
        "build_white_fairies",
        "coloring_silver_fairies",
        "design_purple_fairies",
        "bring_aqua_leprechauns"
    ], f'Неверно найдены задачи для билда {request_data}!'


def test_request_build_without_tasks():
    request_data = {"build": "test_empty_build"}
    with TestClient(app) as client:
        response = client.post(
            "/get_tasks",
            json=request_data
        )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Build has no tasks!"
    }, 'Для билда без задач должна возвращаться соответствующая ошибка!'


def test_request_nonexistent_build():
    request_data = {"build": "nonexistent_build"}
    with TestClient(app) as client:
        response = client.post(
            "/get_tasks",
            json=request_data
        )
    assert response.status_code == 400
    assert response.json() == {
        "detail": 'Build name (nonexistent_build) not found in builds.yaml!'
    }, 'Для несуществующего билда должна возвращаться соответствующая ошибка!'


def test_request_without_build_key():
    request_data = {"not_build": "dont matter value"}
    with TestClient(app) as client:
        response = client.post(
            "/get_tasks",
            json=request_data
        )
    assert response.status_code == 400
    assert response.json() == {
        "detail": 'Invalid JSON key! Expected key: "build".'
    }, ('При отсутствии в запросе ключа "build" должна возвращаться '
        'соответствующая ошибка!')


def test_request_with_wrong_build_type():
    request_data = {"build": 1}
    with TestClient(app) as client:
        response = client.post(
            "/get_tasks",
            json=request_data
        )
    assert response.status_code == 400
    assert response.json() == {
        "detail": 'Invalid JSON value! Must be a string.'
    }, ('При неверном типе значения build должна возвращаться '
        'соответствующая ошибка!')
