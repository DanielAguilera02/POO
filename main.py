import pymysql

class DataBase:
    def __init__(self) -> None:
        self.connection=pymysql.connect(
            host='localhost', 
            user='root',
            password='root',
            db='articulo'
        )
        self.cursor=self.connection.cursor()
        print("conexión establecida")
        
database=DataBase()
