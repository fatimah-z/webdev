import json
from app import app
from app.models import Users
from app import get_db_session


@app.route('/')
def home():
     return "Hello, World!"

@app.route('/user')
def index():
    with get_db_session() as db_session:
        new_user = Users(name="fatima", password="pass")
        db_session.add(new_user)
        db_session.commit()
    return "New user added"

@app.route('/users')
def get_users():
    with get_db_session() as db_session:
        users = db_session.query(Users).all()
        result = [user.to_json() for user in users]
        return result
    
