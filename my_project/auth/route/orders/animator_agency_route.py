from http import HTTPStatus
from flask import Blueprint, jsonify, make_response

from my_project.auth.controller import animator_agency_controller

animator_agency_bp = Blueprint('animator_agency', __name__, url_prefix='/animator_agency')

@animator_agency_bp.get('/agency/<int:agency_id>')
def get_animators_by_agency(agency_id: int):
    """
    Gets all animators for a specific agency.
    """
    animators = animator_agency_controller.get_animators_by_agency(agency_id)
    return make_response(jsonify(animators), HTTPStatus.OK)

@animator_agency_bp.get('/animator/<int:animator_id>')
def get_agencies_by_animator(animator_id: int):
    """
    Gets all agencies for a specific animator.
    """
    agencies = animator_agency_controller.get_agencies_by_animator(animator_id)
    return make_response(jsonify(agencies), HTTPStatus.OK)
@animator_agency_bp.get('/')
def get_all_relationships():
    """
    Gets all relationships in the animator_agency table.
    """
    relationships = animator_agency_controller.get_all_relationships()
    return make_response(jsonify(relationships), HTTPStatus.OK)