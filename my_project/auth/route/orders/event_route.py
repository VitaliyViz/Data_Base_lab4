from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import event_controller
from my_project.auth.domain import Event

event_bp = Blueprint('event', __name__, url_prefix='/event')

@event_bp.get('')
def get_all_events() -> Response:
    return make_response(jsonify(event_controller.find_all()), HTTPStatus.OK)

@event_bp.post('')
def create_event() -> Response:
    content = request.get_json()
    event = Event.create_from_dto(content)
    event_controller.create(event)
    return make_response(jsonify(event.put_into_dto()), HTTPStatus.CREATED)

@event_bp.get('/<int:event_id>')
def get_event(event_id: int) -> Response:
    return make_response(jsonify(event_controller.find_by_id(event_id)), HTTPStatus.OK)

@event_bp.put('/<int:event_id>')
def update_event(event_id: int) -> Response:
    content = request.get_json()
    event = Event.create_from_dto(content)
    event_controller.update(event_id, event)
    return make_response("Event updated", HTTPStatus.OK)

@event_bp.delete('/<int:event_id>')
def delete_event(event_id: int) -> Response:
    event_controller.delete(event_id)
    return make_response("Event deleted", HTTPStatus.OK)
