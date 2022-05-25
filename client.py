from fastapi import Depends
from database import SessionLocal

from telethon import TelegramClient
from telethon.tl import types
from telethon.sync import events
from views import create_entity
from services import get_db, get_entity_by_telegram_id
import schemas
import asyncio
import asyncpg

API_ID = "5007811"
API_HASH = "2cda9777e4c54c921f49a80d7f5b99ee"

client = TelegramClient("session_name", API_ID, API_HASH).start()


async def client_init() -> TelegramClient:
    client = TelegramClient("session_name", API_ID, API_HASH)
    return await client.start()



# async def run_client():
#     if not await client.is_user_authorized():
#         print(123)
    
#     # tg_dialogs = await client.get_dialogs()
#     # for dialog in tg_dialogs:
#     #     await new_entity(dialog.entity, SessionLocal, client)
#     # await client.disconnect()
#     await client.run_until_disconnected()


# async def notify_about_new_message(event):
#     print(event)

async def _get_chat_values(entity):
    return (entity.title, entity.id, True, False, False)

async def _get_user_values(entity):
    firstname = entity.first_name or 'Удаленный акаунт'
    return (firstname, entity.id, False, False, True)

async def _get_channel_values(entity):
    return (entity.title, entity.id, False, True, False)


entity_types_manager = {
    "Chat": _get_chat_values,
    "User": _get_user_values,
    "Channel": _get_channel_values,

}

async def new_entity(entity, db: SessionLocal, client: TelegramClient):
    # if await get_entity_by_telegram_id(db, entity.id) == 0 and entity.id != 939963840:
        # entity_values = await entity_types_manager[entity.__class__.__name__](entity)
        # conn = await asyncpg.connect(user='pluragramv2', password='pluragramv2',
        #                             database='pluragramv2', host='localhost', port=5433)
        

        # await conn.execute(
        #     '''INSERT INTO entities(name, telegram_id, is_group, is_channel, is_user) VALUES($1, $2, $3, $4, $5);''', entity_values[0], entity_values[1], entity_values[2], entity_values[3], entity_values[4]
        # )
        # await conn.close()

    async for message in client.iter_messages(entity, reverse=True, limit=100):
        if not isinstance(message, types.MessageActionChatJoinedByLink) or not isinstance(message, types.MessageActionContactSignUp) or not isinstance(message, types.MessageActionChannelMigrateFrom):
            if await get_entity_by_telegram_id(db, message.sender_id) == 0:


                conn = await asyncpg.connect(user='pluragramv2', password='pluragramv2',
                                            database='pluragramv2', host='localhost', port=5433)
                
            

                await conn.execute(
                    '''INSERT INTO entities(name, telegram_id, is_group, is_channel, is_user) VALUES($1, $2, $3, $4, $5);''', message.sender_id[0], entity_values[1], entity_values[2], entity_values[3], entity_values[4]
                )
                await conn.close()

            # await conn.execute(
            #     '''INSERT INTO messages(text, telegram_id, entity_id) VALUES($1, $2, $3);''', message.message, message.id, entity.id
            # )
            # await conn.close()


