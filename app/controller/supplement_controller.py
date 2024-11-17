from .general_controller import GeneralController
from ..service import supplement_service

class SupplementController(GeneralController):
    _service = supplement_service
