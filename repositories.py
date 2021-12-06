import models


class DoctorRepository:

    def __init__(self):
        pass

    @staticmethod
    def find_all_doctors(db):
        records = db.query(models.Doctor).all()
        return records
