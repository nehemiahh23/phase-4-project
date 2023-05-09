from flask import Flask, request, make_response, jsonify, session
from flask_migrate import Migrate

from models import db, Owner, Pet, Doctor, Appointment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app,db)

db.init_app(app)

def authorize():
    user_id = session["user_id"]
    current_user = Owner.query.get(user_id)
    if not current_user:
        return {'error': 'Not logged in'}, 401

#Check Session


#Owner Login
@app.post('/ownerlogin')
def owner_login():
    json = request.json
    current_owner = Owner.query.where(Owner.username == json['username']).first()
    if (current_owner):
        return current_owner.to_dict(), 201
    else:
        return {'message': "Invalid username or password"}, 401

#Owner Logout
#Owner Create Account
@app.post('/ownercreate')
def create_account():
    json = request.json
    new_owner = Owner(email=json['email'], name = json['name'], username = json['username'], password = json['password'])
    db.session.add(new_owner)
    db.session.commit()
    session['user_id'] = new_owner.id
    return new_owner.to_dict(), 201

#Doctor Login
@app.post('/doctorlogin')
def doctor_login():
    json = request.json
    current_doctor = Doctor.query.where(Doctor.username == json['username']).first()
    if (current_doctor):
        return current_doctor.to_dict(), 201
    else:
        return {'message': 'Invalid username or password'}, 401





#Doctor Logout


@app.route('/')
def home():
    return ''




if __name__ == '__main__':
    app.run(port=5555, debug=True)