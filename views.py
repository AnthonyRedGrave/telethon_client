from sqlalchemy.orm import Session
import schemas

async def create_entity(db: Session, entity: schemas.CreateEntity):
    print(db)
    print(entity)