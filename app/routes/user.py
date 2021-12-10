from fastapi import APIRouter
from app.config.db import conn
from app.model.index import users
from app.schema.index import User
from app.utils.fastapi_utils import repeat_every
from datetime import datetime
user=APIRouter()
# import schedule
# import time
# @user.get("/")
# async def read_data():
#     return conn.execute(users.select()).fetchall()



@user.get("/{id}")
async def read_data(id:int):
    return conn.execute(users.select().where(users.c.id==id)).fetchall()   

@user.post("/")
async def write_data(user:User):
    conn.execute(users.insert().values(
        name=user.name,
        email=user.email
    ))
    return conn.execute(users.select()).fetchall()

@user.put("/{id}")
async def update_data(id:int,user:User):
    conn.execute(users.update().values(
        name=user.name,
        email=user.email
    ).where(users.c.id==id))
    return conn.execute(users.select()).fetchall()  

@user.on_event("startup")      
@repeat_every(seconds=60)  
@user.get("/")
async def root():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    return {"Hello world,the server is running"}

# schedule.every(1).seconds.do(root)