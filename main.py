import models
from database import SessionLocal, engine


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def show_records(db):
    records = db.query(models.Doctor).all()
    return records


def main():
    try:
        db = SessionLocal()
        # yield db
        result = show_records(db)
        for record in result:
            print(record.first_name)
    finally:
        db.close()


if __name__ == "__main__":
    main()
