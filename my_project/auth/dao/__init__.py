"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# orders DB
# from .orders.client_dao import ClientDAO
# from .orders.client_type_dao import ClientTypeDAO
from .orders.agencies_dao import AgenciesDAO
from .orders.animator_dao import AnimatorDAO
from .orders.event_dao import EventDAO
from .orders.event_type_dao import EventTypeDAO
from .orders.animator_agency_dao import AnimatorAgencyDAO
from .orders.payment_dao import PaymentDAO
from .orders.order_dao import OrderDAO


# client_dao = ClientDAO()
# client_type_dao = ClientTypeDAO()
agencies_dao = AgenciesDAO()
animator_dao = AnimatorDAO()
event_dao = EventDAO()
event_type_dao = EventTypeDAO()
animator_agency_dao = AnimatorAgencyDAO()
payment_dao = PaymentDAO()
order_dao = OrderDAO()