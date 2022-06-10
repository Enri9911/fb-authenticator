from flask import Flask
from repository.user_repository import UserRepository
from firebase.app import initialize_firebase_app

initialize_firebase_app()

app = Flask(__name__)


@app.route('/user/create', methods=['POST'])
def create_user():
    return UserRepository().create_user()


@app.route('/user/verifyEmail', methods=['POST'])
def send_verification_email():
    return UserRepository().verify_email()


@app.route('/user/resetPassword', methods=['POST'])
def send_reset_password_link():
    return UserRepository().reset_password()


@app.route('/user/<uid>', methods=['GET'])
def get_user():
    return UserRepository().get_user()


app.run(host='0.0.0.0', port=8080, debug=True)
