from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from app.config.db import meta
users=Table(
    'users',meta,
    Column('id',Integer,primary_key=True),
    Column('name',String(45)),
    Column('email',String(45))


)
