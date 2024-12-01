"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import order_controller
from my_project.auth.domain import Order

order_bp = Blueprint('order', __name__, url_prefix='/order')


@order_bp.get('')
def get_all_orders() -> Response:
    """
    Gets all objects from table using Order layer.
    :return: Response object
    """
    return make_response(jsonify(order_controller.find_all()), HTTPStatus.OK)


@order_bp.post('')
def create_order() -> Response:
    """
    Creates a new order.
    :return: Response object
    """
    content = request.get_json()
    order = Order.create_from_dto(content)
    order_controller.create(order)
    return make_response(jsonify(order.put_into_dto()), HTTPStatus.CREATED)


@order_bp.get('/<int:order_id>')
def get_order(order_id: int) -> Response:
    """
    Gets an order by ID.
    :return: Response object
    """
    return make_response(jsonify(order_controller.find_by_id(order_id)), HTTPStatus.OK)


@order_bp.put('/<int:order_id>')
def update_order(order_id: int) -> Response:
    """
    Updates an order by ID.
    :return: Response object
    """
    content = request.get_json()
    order = Order.create_from_dto(content)
    order_controller.update(order_id, order)
    return make_response("Order updated", HTTPStatus.OK)


@order_bp.delete('/<int:order_id>')
def delete_order(order_id: int) -> Response:
    """
    Deletes an order by ID.
    :return: Response object
    """
    order_controller.delete(order_id)
    return make_response("Order deleted", HTTPStatus.OK)


@order_bp.get('/status/<string:status>')
def get_orders_by_status(status: str) -> Response:
    """
    Gets orders filtered by status.
    :return: Response object
    """
    return make_response(jsonify(order_controller.find_by_status(status)), HTTPStatus.OK)


@order_bp.get('/above-cost/<float:min_cost>')
def get_orders_above_cost(min_cost: float) -> Response:
    """
    Gets orders with cost above a specified value.
    :return: Response object
    """
    return make_response(jsonify(order_controller.get_orders_above_cost(min_cost)), HTTPStatus.OK)
