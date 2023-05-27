from app import app

app.testing = True
client = app.test_client()

def test_index():
    response = client.get('/')
    assert b"Hello, World!" in response.data
