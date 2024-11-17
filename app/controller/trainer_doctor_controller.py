from .general_controller import GeneralController
from ..service import trainer_doctor_service, schedule_service

class TrainerDoctorController(GeneralController):
    _service = trainer_doctor_service

    def get_schedules_for_trainer_doctor(self, trainer_doctor_id: int):
        return [schedule.put_into_dto() for schedule in schedule_service.find_by_trainer_doctor_id(trainer_doctor_id)]
