from abc import ABCMeta, abstractmethod


class IConnection(metaclass=ABCMeta):
    @abstractmethod
    def get_connection(self):
        """implements in child class"""


class SnowflakeDBConnection(IConnection):

    __instance = None

    def __init__(self, *args, **kwargs):
        if SnowflakeDBConnection.__instance is not None:
            raise Exception("DB Connection is already instantiated")
        # print(args[0])
        self.account = kwargs["account"]
        SnowflakeDBConnection.__instance = self

    @staticmethod
    def get_instance():
        if SnowflakeDBConnection.__instance is None:
            SnowflakeDBConnection(account="test")
        return SnowflakeDBConnection.__instance

    def get_connection(self):
        print(f"URI : {SnowflakeDBConnection.__instance.account}")


class PostgresDBConnection(IConnection):

    __instance = None

    @staticmethod
    def get_instance():
        if PostgresDBConnection.__instance is None:
            PostgresDBConnection(host="127.0.0.1")
        return PostgresDBConnection.__instance

    def __init__(self, *args, **kwargs):
        if PostgresDBConnection.__instance is not None:
            raise Exception("DB Connection is already instantiated")
        # print(args[0])
        self.host = kwargs["host"]
        PostgresDBConnection.__instance = self

    def get_connection(self):
        print(f"URI : {PostgresDBConnection.__instance.host}")


class DBFactory:
    # def __init__(self, db_type):
    #     self.type = db_type

    @staticmethod
    def get_db(*args, **kwargs):
        return eval(args[0])(*args, **kwargs)
        # if self.type == "snowflake":
        #     return SnowflakeDBConnection(*args, **kwargs)
        # elif self.type == "postgres":
        #     return PostgresDBConnection(*args, **kwargs)


if __name__ == "__main__":
    #
    # d1 = SnowflakeDBConnection(account="test")
    # d1.get_connection()
    # # d2 = PostgresDBConnection.get_instance()
    # # d2.get_connection()
    #
    # p1 = PostgresDBConnection.get_instance()
    # p1.get_connection()

    f1 = DBFactory()
    get_entity = f1.get_db("PostgresDBConnection", host="192.168.12.123")
    get_entity.get_connection()

    get_snow_entity = f1.get_db("SnowflakeDBConnection", account="kell")
    get_snow_entity.get_connection()
