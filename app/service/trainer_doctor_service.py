from .general_service import GeneralService
from ..dao import trainer_doctor_dao


class TrainerDoctorService(GeneralService):
    _dao = trainer_doctor_dao
