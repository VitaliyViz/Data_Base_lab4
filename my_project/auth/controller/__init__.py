"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# from .orders.client_controller import ClientController
# from .orders.client_type_controller import ClientTypeController
from .orders.agencies_controller import AgenciesController
from .orders.animator_controller import AnimatorController
from .orders.event_controller import EventController
from .orders.event_type_controller import EventTypeController
from .orders.animator_agency_controller import AnimatorAgencyController


# client_controller = ClientController()
# client_type_controller = ClientTypeController()
agencies_controller = AgenciesController()
animator_controller = AnimatorController()
event_controller = EventController()
event_type_controller = EventTypeController()
animator_agency_controller = AnimatorAgencyController()