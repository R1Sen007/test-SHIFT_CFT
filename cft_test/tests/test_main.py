from fastapi.testclient import TestClient

from app.api import app
from .persons import person_1


client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_wrong_password():
    response = client.post("/users/login", data={"username": person_1.username, "password": "incorrect_password"})
    '''
    Incorrect password
    '''
    assert response.status_code == 401, "Wrong response"


def test_get_token():
    response = client.post("/users/login", data={"username": person_1.username, "password": person_1.password})
    '''
    Correct password, get token
    '''
    assert response.status_code == 200, "Wrong response"
    person_1.token = response.json()["access_token"]
    print(person_1.token)


def test_not_auth():
    response = client.get("/users/salary")
    '''
    Get salary with no token
    '''
    assert response.status_code == 401, "Wrong response"


def test_bad_token():
    response = client.get("/users/salary", headers={"Authorization": f"Bearer b@d_t0ken"})
    '''
    Get salary with bad token
    '''
    assert response.status_code == 401, "Wrong response"


def test_salary_info():
    response = client.get("/users/salary", headers={"Authorization": f"Bearer {person_1.token}"})
    response_data = response.json()


    assert response.status_code == 200, "Wrong response"
    assert response_data["salary"] == 40000, "Wrong salary"
    assert response_data["date_increase"] == "2023-12-12", "Wrong date increase"



