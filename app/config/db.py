from sqlalchemy import create_engine,MetaData

engine=create_engine("mysql+pymysql://manisha:Jingjung31_12@127.0.0.1/eunimart")
meta=MetaData()
conn=engine.connect()