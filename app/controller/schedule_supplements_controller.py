from .general_controller import GeneralController
from ..service import schedule_supplements_service, supplement_service

class ScheduleSupplementsController(GeneralController):
    _service = schedule_supplements_service

    def get_supplements(self, schedule_supplements_id: int):
        return supplement_service.find_by_schedule_supplements_id(schedule_supplements_id)
