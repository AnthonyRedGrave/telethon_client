import sqlalchemy as _sql
from sqlalchemy.orm import relationship
import database

class Entity(database.Base):
    """User, Chat or Channel"""
    __tablename__ = "entities"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    is_user = _sql.Column(_sql.Boolean, default=_sql.false)
    is_dialog = _sql.Column(_sql.Boolean, default=_sql.false)
    is_contact = _sql.Column(_sql.Boolean, default=_sql.false)
    is_channel = _sql.Column(_sql.Boolean, default=_sql.false)
    is_group = _sql.Column(_sql.Boolean, default=_sql.false)
    is_gpc = _sql.Column(_sql.Boolean, default=_sql.false)
    is_active = _sql.Column(_sql.Boolean, default=_sql.false)
    is_bot = _sql.Column(_sql.Boolean, default=_sql.false)
    is_deleted = _sql.Column(_sql.Boolean, default=_sql.false)
    telegram_id = _sql.Column(_sql.BigInteger, nullable=_sql.null)
    name = _sql.Column(_sql.String)
    phone = _sql.Column(_sql.String)
    username = _sql.Column(_sql.String)
    messages = relationship("Message", back_populates='entity')

    def __str__(self):
        return self.name


class Message(database.Base):
    """Message"""
    __tablename__ = "messages"

    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    text = _sql.Column(_sql.String)
    telegram_id = _sql.Column(_sql.BigInteger, nullable=_sql.null)
    entity_id = _sql.Column(_sql.BigInteger, _sql.ForeignKey("entities.id"))
    entity = relationship("Entity", back_populates='messages')
    sender_id = _sql.Column(_sql.BigInteger, _sql.ForeignKey("entities.id"))