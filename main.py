from pydoc import cli
from fastapi import FastAPI
from typing import TYPE_CHECKING, List
from client import client_init, client



app = FastAPI()

if __name__ == '__main__':
    client.start()
    print("started")
    client.run_until_disconnected()



