import datetime
from email import *
from fastapi.testclient import TestClient
from .. import main
from main import app

client = TestClient(app)

def test_read_users():
    response = client.get("/newsletter/")
    assert response.status_code == 200
    assert response.json() != None

def test_insert_new_users():
    email = f'{datetime.date.today()}@test.com'
    response = client.post(
        "/newsletter/",
        json={"name": "Hola","email": email,"birth_date": "1993-06-27","sennior_client": "true","subscripted_date": "2022-06-27"}
    )

    assert response.status_code == 200
    assert response.json() == {'name': 'Hola', 'email': email, 'birth_date': '1993-06-27', 'sennior_client': True, 'subscripted_date': '27/06/2022'}

if __name__ == '__main__':
    test_read_users()
    test_insert_new_users()
    print("Todos los test se han ejecutado correctamente")
