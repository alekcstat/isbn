from flask import Blueprint, request, jsonify
from services.user_service import UserService

user_api = Blueprint('user_api', __name__)

@user_api.route('/api/user', methods=['POST'])
def create_user_controller():

    data = request.get_json()
    UserService.create_user_service(data)

    return jsonify("User has been successfully created."), 201