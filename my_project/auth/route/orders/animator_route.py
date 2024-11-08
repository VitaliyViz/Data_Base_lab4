from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import animator_controller
from my_project.auth.domain.orders.animator import Animator

animator_bp = Blueprint('animator', __name__, url_prefix='/animator')

@animator_bp.get('')
@animator_bp.get('')
def get_all_animators() -> Response:
    """
    Gets all animators from the database.
    :return: Response object
    """
    animator = animator_controller.find_all()  
    animator_dto = [animator.put_into_dto() for animator in animator]
    return make_response(jsonify(animator_dto), HTTPStatus.OK)

@animator_bp.post('')
def create_animator() -> Response:
    """
    Creates a new animator in the database.
    :return: Response object
    """
    content = request.get_json()
    animator = Animator.create_from_dto(content)
    animator_controller.create_animator(animator) 
    return make_response(jsonify(animator.put_into_dto()), HTTPStatus.CREATED)

@animator_bp.get('/<int:animator_id>')
def get_animator(animator_id: int) -> Response:
    """
    Gets animator by ID.
    :return: Response object
    """
    animator = animator_controller.find_by_id(animator_id)
    if animator:
        return make_response(jsonify(animator.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Animator not found"}), HTTPStatus.NOT_FOUND)

@animator_bp.put('/<int:animator_id>')
def update_animator(animator_id: int) -> Response:
    """
    Updates animator by ID.
    :return: Response object
    """
    content = request.get_json()
    animator = Animator.create_from_dto(content)
    animator_controller.update_animator(animator_id, animator)
    return make_response("Animator updated", HTTPStatus.OK)

@animator_bp.delete('/<int:animator_id>')
def delete_animator(animator_id: int) -> Response:
    """
    Deletes animator by ID.
    :return: Response object
    """
    animator_controller.delete_animator(animator_id)
    return make_response("Animator deleted", HTTPStatus.NO_CONTENT)

@animator_bp.get('/name/<string:name>')
def get_animator_by_name(name: str) -> Response:
    """
    Gets animator by name.
    :param name: Animator name
    :return: Response object
    """
    animator = animator_controller.get_animator_by_name(name)
    return make_response(jsonify([animator.put_into_dto() for animator in animator]), HTTPStatus.OK)

@animator_bp.get('/phone/<string:phone>')
def get_animator_by_phone(phone: str) -> Response:
    """
    Gets animator by phone.
    :param phone: Animator phone number
    :return: Response object
    """
    animator = animator_controller.get_animator_by_phone(phone)
    return make_response(jsonify([animator.put_into_dto() for animator in animator]), HTTPStatus.OK)