from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import event_type_controller
from my_project.auth.domain import EventType

event_type_bp = Blueprint('event_types', __name__, url_prefix='/event-types')

@event_type_bp.get('')
def get_all_event_types() -> Response:
    return make_response(jsonify(event_type_controller.find_all()), HTTPStatus.OK)

@event_type_bp.post('')
def create_event_type() -> Response:
    content = request.get_json()
    event_type = EventType.create_from_dto(content)
    event_type_controller.create(event_type)
    return make_response(jsonify(event_type.put_into_dto()), HTTPStatus.CREATED)

@event_type_bp.get('/<int:event_type_id>')
def get_event_type(event_type_id: int) -> Response:
    return make_response(jsonify(event_type_controller.find_by_id(event_type_id)), HTTPStatus.OK)

@event_type_bp.put('/<int:event_type_id>')
def update_event_type(event_type_id: int) -> Response:
    content = request.get_json()
    event_type = EventType.create_from_dto(content)
    event_type_controller.update(event_type_id, event_type)
    return make_response("Event Type updated", HTTPStatus.OK)

@event_type_bp.delete('/<int:event_type_id>')
def delete_event_type(event_type_id: int) -> Response:
    event_type_controller.delete(event_type_id)
    return make_response("Event Type deleted", HTTPStatus.OK)

@event_type_bp.get('/find-by-name/<string:name>')
def find_event_type_by_name(name: str) -> Response:
    return make_response(jsonify(event_type_controller.find_by_name(name)), HTTPStatus.OK)

@event_type_bp.get('/find-by-email/<string:email>')
def find_event_type_by_email(email: str) -> Response:
    return make_response(jsonify(event_type_controller.find_by_email(email)), HTTPStatus.OK)
