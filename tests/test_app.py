from http import HTTPStatus

from fastapi.testclient import TestClient

from src.fastapi_zero_deploy.app import app


def test_root_deve_retornar_ok_e_ola_mund0():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo!"}
