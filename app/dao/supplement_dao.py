from .. import db
from ..domain.supplement import Supplement

class SupplementDAO:
    @staticmethod
    def find_all():
        return Supplement.query.all()

    @staticmethod
    def find_by_id(supplement_id):
        supplement = Supplement.query.get(supplement_id)
        if supplement:
            db.session.refresh(supplement)
        return supplement

    @staticmethod
    def create(supplement):
        db.session.add(supplement)
        db.session.commit()
        return supplement

    @staticmethod
    def update(supplement_id, new_supplement):
        supplement = Supplement.query.get(supplement_id)
        if supplement:
            for key, value in vars(new_supplement).items():
                if key != 'id' and value is not None:
                    setattr(supplement, key, value)
            db.session.commit()
        return supplement

    @staticmethod
    def patch(supplement_id, updates):
        supplement = Supplement.query.get(supplement_id)
        if supplement:
            for key, value in updates.items():
                setattr(supplement, key, value)
            db.session.commit()
        return supplement

    @staticmethod
    def put(supplement_id, new_data):
        supplement = Supplement.query.get(supplement_id)
        if supplement:
            for key in vars(supplement):
                if key != 'id':
                    setattr(supplement, key, new_data.get(key, None))
            db.session.commit()
        return supplement

    @staticmethod
    def delete(supplement_id):
        supplement = Supplement.query.get(supplement_id)
        if supplement:
            db.session.delete(supplement)
            db.session.commit()
            return True
        return False

    @staticmethod
    def delete_all():
        Supplement.query.delete()
        db.session.commit()
