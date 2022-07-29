
import psycopg2

try:
    connection = psycopg2.connect(user="user_test",
                                  password="StratApps$09",
                                  host="138.68.44.49",
                                  port="5432",
                                  database="TestingDB")
    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from store_emp"

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from store_emp table using cursor.fetchall\n")
    mobile_records = cursor.fetchall()

    print("Print each row and it's columns values")
    for row in mobile_records:
        print("\nEname = ", row[0], )
        print("Eid = ", row[1])
        print("job  = ", row[2])
        print("job  = ", row[3],'\n')

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")