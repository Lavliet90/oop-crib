class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Cоединение с бд: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('Закрытие соединения с бд')

    def read(self):
        return 'Данные из бд'

    def write(self, data):
        print(f'Записьв бд {data}')


db = DataBase('yan', '1234', 90)
db2 = DataBase('ang', '3454', 40)

print(id(db), id(db2))

db.connect()
db2.connect()
