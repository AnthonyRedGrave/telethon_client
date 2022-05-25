from uvicorn.workers import UvicornWorker
from telethon import TelegramClient
from telethon.tl import types
from telethon.sync import events


API_ID = "5007811"
API_HASH = "2cda9777e4c54c921f49a80d7f5b99ee"



class MyUvicornWorker(UvicornWorker):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        print("INIT CLIENT")

    async def get():
        
        
        for event, callback in default_events:
                        client.add_event_handler(callback, event)

        await client.connect() 



async def notify_about_new_message(event):
    print(event)

async def notify_about_message_read(event):
    print(event)


default_events = ((events.NewMessage(), notify_about_new_message),
                #   (events.Raw(UpdateChannel), notify_about_chat_action_raw),
                #   (events.ChatAction(), notify_about_chat_action),
                  (events.MessageRead(inbox=True), notify_about_message_read),
                #   (events.UserUpdate(), notify_about_user_update),
                #   (events.MessageDeleted(), notify_about_deleted_message)
)