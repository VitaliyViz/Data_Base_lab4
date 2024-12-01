"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# from .orders.client_service import ClientService
# from .orders.client_type_service import ClientTypeService
from .orders.agencies_service import AgenciesService
from .orders.animator_service import AnimatorService
from .orders.event_service import EventService
from .orders.event_type_service import EventTypeService
from .orders.animator_agency_service import AnimatorAgencyService
from .orders.payment_service import PaymentService
from .orders.order_service import OrderService

# client_service = ClientService()
# client_type_service = ClientTypeService()
agencies_service = AgenciesService()
animator_service = AnimatorService()
event_service = EventService()
event_type_service = EventTypeService()
animator_agency_service = AnimatorAgencyService()
payment_service = PaymentService()
order_service = OrderService()