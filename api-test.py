from email import header
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_users():
    response = client.get("/newsletter/")
    assert response.status_code == 200
    assert response.json() != None

def test_insert_new_users():
    response = client.post(
        "/newsletter/",
        json={},
    )
    print(response.status_code)
    assert response.status_code == 200
    
    assert response.json() == {
        "name": "Adrian",
        "email": "adri@test.com",
        "birth_date": "1993-07-13",
        "sennior_client": "true",
        "subscripted_date": "27/06/2022"
        }

if __name__ == '__main__':
    test_read_users()
    test_insert_new_users()
    print("Todos los test se han ejecutado correctamente")
