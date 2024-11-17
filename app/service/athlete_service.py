from .general_service import GeneralService
from ..dao import athlete_dao


class AthleteService(GeneralService):
    _dao = athlete_dao
