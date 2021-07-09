import psycopg2
from psycopg2 import pool
import time
start = time.time()
try:
    threaded_postgreSQL_pool = psycopg2.pool.ThreadedConnectionPool(1, 20, user="postgres",
                                                                    password="my_password",
                                                                    host="127.0.0.1",
                                                                    port="54320",
                                                                    database="postgres")
    if (threaded_postgreSQL_pool):
        print("Connection pool created successfully using ThreadedConnectionPool")

    # Use getconn() method to Get Connection from connection pool
    ps_connection = threaded_postgreSQL_pool.getconn()

    if (ps_connection):

        print("successfully recived connection from connection pool ")
        ps_cursor = ps_connection.cursor()
        ps_cursor.execute("select * from products")
        mobile_records = ps_cursor.fetchmany(2)

        print("Displaying rows from mobile table")
        for row in mobile_records:
            print(row)

        ps_cursor.close()

        # Use this method to release the connection object and send back ti connection pool
        threaded_postgreSQL_pool.putconn(ps_connection)
        print("Put away a PostgreSQL connection")

except (Exception, psycopg2.DatabaseError) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    # closing database connection.
    # use closeall() method to close all the active connection if you want to turn of the application
    if threaded_postgreSQL_pool:
        threaded_postgreSQL_pool.closeall
    print("Threaded PostgreSQL connection pool is closed")

end = time.time()

print(end-start)