import psycopg2
from psycopg2 import Error
import time

start = time.time()
try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="my_password",
                                  host="127.0.0.1",
                                  port="54320",
                                  database="postgres")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT * from products")
    # Fetch result
    # record = cursor.fetchone()
    mobile_records = cursor.fetchmany(2)

    print("Displaying rows from mobile table")
    for row in mobile_records:
        print(row)
    # print("You are connected to - ", record, "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

end = time.time()
print(end - start)