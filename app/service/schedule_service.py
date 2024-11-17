from .general_service import GeneralService
from ..dao import schedule_dao


class ScheduleService(GeneralService):
    _dao = schedule_dao
