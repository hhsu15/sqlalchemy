# from fastapi import FastAPI
import asyncio
import time
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer


app = FastAPI()


# @app.get("/")
# async def read_root():
#     print("Received request home!")
#     data = await get_data()

#     # time.sleep(5)
#     print("data:", data)
#     return data


# async def get_data():
#     await asyncio.sleep(10)
#     return "Some data"


# @app.get("/sync")
# def read_root():
#     print("Received sync request!")
#     time.sleep(10)
#     # time.sleep(5)
#     print("Hey is done")
#     return {"Hello": "World"}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
