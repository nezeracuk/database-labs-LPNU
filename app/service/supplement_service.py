from .general_service import GeneralService
from ..dao import supplement_dao


class SupplementService(GeneralService):
    _dao = supplement_dao
