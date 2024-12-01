"""
2024
apavelchak@gmail.com
© Andrii Pavelchak
"""
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import payment_controller
from my_project.auth.domain import Payment

payment_bp = Blueprint('payment', __name__, url_prefix='/payment')


@payment_bp.get('')
def get_all_payments() -> Response:
    """
    Gets all payment objects.
    :return: Response object
    """
    return make_response(jsonify(payment_controller.find_all()), HTTPStatus.OK)


@payment_bp.post('')
def create_payment() -> Response:
    """
    Creates a new payment record.
    :return: Response object
    """
    content = request.get_json()
    payment = Payment.create_from_dto(content)
    payment_controller.create(payment)
    return make_response(jsonify(payment.put_into_dto()), HTTPStatus.CREATED)


@payment_bp.get('/<int:payment_id>')
def get_payment(payment_id: int) -> Response:
    """
    Gets payment by ID.
    :param payment_id: Payment ID
    :return: Response object
    """
    return make_response(jsonify(payment_controller.find_by_id(payment_id)), HTTPStatus.OK)


@payment_bp.put('/<int:payment_id>')
def update_payment(payment_id: int) -> Response:
    """
    Updates payment by ID.
    :param payment_id: Payment ID
    :return: Response object
    """
    content = request.get_json()
    payment = Payment.create_from_dto(content)
    payment_controller.update(payment_id, payment)
    return make_response("Payment updated", HTTPStatus.OK)


@payment_bp.delete('/<int:payment_id>')
def delete_payment(payment_id: int) -> Response:
    """
    Deletes payment by ID.
    :param payment_id: Payment ID
    :return: Response object
    """
    payment_controller.delete(payment_id)
    return make_response("Payment deleted", HTTPStatus.OK)


@payment_bp.get('/find-by-order/<int:order_id>')
def find_payments_by_order(order_id: int) -> Response:
    """
    Finds payments by Order ID.
    :param order_id: Order ID
    :return: Response object
    """
    return make_response(jsonify(payment_controller.find_by_order_id(order_id)), HTTPStatus.OK)


@payment_bp.get('/find-by-status/<string:status>')
def find_payments_by_status(status: str) -> Response:
    """
    Finds payments by status.
    :param status: Payment status
    :return: Response object
    """
    return make_response(jsonify(payment_controller.find_by_status(status)), HTTPStatus.OK)
