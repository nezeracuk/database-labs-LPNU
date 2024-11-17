from abc import ABC
from typing import List, Dict, Any

class GeneralService(ABC):
    _dao = None

    def find_all(self) -> List[object]:
        return [obj.put_into_dto() for obj in self._dao.find_all()]

    def find_by_id(self, key: int) -> object:
        return self._dao.find_by_id(key).put_into_dto()

    def create(self, obj: object) -> object:
        return self._dao.create(obj).put_into_dto()

    def create_all(self, obj_list: List[object]) -> List[object]:
        return self._dao.create_all(obj_list)

    def update(self, key: int, obj: object) -> None:
        self._dao.update(key, obj)

    def patch(self, key: int, updates: Dict[str, Any]) -> None:
        obj = self._dao.find_by_id(key)
        if obj:
            for field_name, value in updates.items():
                setattr(obj, field_name, value)
            self._dao.update(key, obj)

    def delete(self, key: int) -> None:
        self._dao.delete(key)

    def delete_all(self) -> None:
        self._dao.delete_all()
