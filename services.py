from sqlalchemy.orm import Session
import database
import models
from database import SessionLocal

def _add_tables():
    return database.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_entity_by_telegram_id(db: SessionLocal, telegram_id: int):
    db = db()
    return db.query(models.Entity).filter(models.Entity.telegram_id == telegram_id).count()