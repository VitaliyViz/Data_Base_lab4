from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import agencies_controller
from my_project.auth.domain.orders.agencies import Agencies

agencies_bp = Blueprint('agencies', __name__, url_prefix='/agencies')

@agencies_bp.get('')
@agencies_bp.get('')
def get_all_agencies() -> Response:
    """
    Gets all agencies from the database.
    :return: Response object
    """
    agencies = agencies_controller.find_all()  
    agencies_dto = [agency.put_into_dto() for agency in agencies]
    return make_response(jsonify(agencies_dto), HTTPStatus.OK)

@agencies_bp.post('')
def create_agency() -> Response:
    """
    Creates a new agency in the database.
    :return: Response object
    """
    content = request.get_json()
    agency = Agencies.create_from_dto(content)
    agencies_controller.create_agency(agency) 
    return make_response(jsonify(agency.put_into_dto()), HTTPStatus.CREATED)

@agencies_bp.get('/<int:agency_id>')
def get_agency(agency_id: int) -> Response:
    """
    Gets agency by ID.
    :return: Response object
    """
    agency = agencies_controller.find_by_id(agency_id)
    if agency:
        return make_response(jsonify(agency.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Agency not found"}), HTTPStatus.NOT_FOUND)

@agencies_bp.put('/<int:agency_id>')
def update_agency(agency_id: int) -> Response:
    """
    Updates agency by ID.
    :return: Response object
    """
    content = request.get_json()
    agency = Agencies.create_from_dto(content)
    agencies_controller.update_agency(agency_id, agency)  # Викликаємо метод для оновлення агенції
    return make_response("Agency updated", HTTPStatus.OK)

@agencies_bp.delete('/<int:agency_id>')
def delete_agency(agency_id: int) -> Response:
    """
    Deletes agency by ID.
    :return: Response object
    """
    agencies_controller.delete_agency(agency_id)  # Викликаємо метод для видалення агенції
    return make_response("Agency deleted", HTTPStatus.NO_CONTENT)

@agencies_bp.get('/name/<string:name>')
def get_agencies_by_name(name: str) -> Response:
    """
    Gets agencies by name.
    :param name: Agency name
    :return: Response object
    """
    agencies = agencies_controller.get_agencies_by_name(name)
    return make_response(jsonify([agency.put_into_dto() for agency in agencies]), HTTPStatus.OK)

@agencies_bp.get('/phone/<string:phone>')
def get_agencies_by_phone(phone: str) -> Response:
    """
    Gets agencies by phone.
    :param phone: Agency phone number
    :return: Response object
    """
    agencies = agencies_controller.get_agencies_by_phone(phone)
    return make_response(jsonify([agency.put_into_dto() for agency in agencies]), HTTPStatus.OK)