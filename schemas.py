import datetime
import pydantic

class _BaseEntity(pydantic.BaseModel):
    user_name: str
    is_user: bool
    is_dialog: bool
    is_contact: bool
    is_channel: bool
    is_group: bool
    is_gpc: bool
    is_active: bool
    is_bot: bool
    is_deleted: bool
    telegram_id: int
    name: str
    phone: str


class Entity(_BaseEntity):
    id: int


class CreateEntity(_BaseEntity):
    pass