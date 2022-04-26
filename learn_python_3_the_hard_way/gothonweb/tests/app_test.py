from app import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert rv.status_code == 404

    rv = web.get('/hello', follow_redirects=True)
    assert rv.status_code == 200
    assert "이 폼을 채우세요" in rv.data.decode()

   #rv = web.get('/hello?name=JY&greet=Welcome', follow_redirects=True)
   #assert rv.status_code == 200
   #assert "이 폼을 채우세요" in rv.data.decode()
   #assert b"JY" in rv.data
   #assert b"Welcome" in rv.data

    data = {'name': 'JY', 'greet': 'Hello!'}
    rv = web.post('/hello', follow_redirects=True, data=data)
    assert "JY" in rv.data.decode()
    assert b"Hello!" in rv.data
