from .general_service import GeneralService
from ..dao import schedule_supplements_dao


class ScheduleSupplementsService(GeneralService):
    _dao = schedule_supplements_dao

