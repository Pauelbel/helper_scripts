import sqlite3


DB_CREDS = {
    "database": "/home/apollon4eg/Repositories/helper_scripts/theory_of_language/oop/sqlite.db"
}


class DBAccessor:
    print("открытие подключения к БД sqlite...")

    def __init__(self, db_creds: dict):
        self.__db_creds = db_creds
        self.__connection = None
        self.__coursor = None

    def __enter__(self):
        if self.__connection is None:
            self.__connection = sqlite3.connect(**self.__db_creds)

        self.__coursor = self.__connection.cursor()
        return self.__coursor

    def __exit__(self, exc_type, exc_value, exc_trace):
        self.__connection.commit()
        self.__connection.close()
        print("соединение с БД закрыто...")


def main():

    with DBAccessor(DB_CREDS) as coursor:
        for row in coursor.execute("SELECT * FROM users"):
            print(row)


if __name__ == "__main__":
    main()
