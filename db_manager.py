import psycopg2
import os
from dotenv import load_dotenv

global connect

load_dotenv()


def open_connection():
    password = os.getenv("PASSWORD")
    try:
        connection = psycopg2.connect(user="postgres",
                                      password=password,
                                      host="127.0.0.1",
                                      port="5432",
                                      database="earthquakes")
        print("PostgreSQL connection is open")
        global connect
        connect = connection
        return connection

    except (Exception, psycopg2.Error) as error:
        print("Failed to connect to database", error)


def select_rows():
    try:
        global connect
        cursor = connect.cursor()
        select_all = """ SELECT * FROM earthquake_schema.earthquakes"""
        cursor.execute(select_all)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        connect.commit()
        count = cursor.rowcount

    except (Exception, psycopg2.Error) as error:
        print("Failed to get records from earthquakes table", error)


def insert_quake(mag, city, time, updated, detail, longitude, latitude, depth, country, id):
    global connect
    cursor = connect.cursor()
    try:
        q = f""""select count(*) from earthquake_schema.earthquakes where id = {id}"""""
        cursor.execute(q)
        result = cursor.fetchone()
        # print(result)
    except (Exception, psycopg2.Error) as error:
        print(str(id), " not present")
        cursor.execute("ROLLBACK")
        connect.commit()
        insert = """INSERT INTO earthquake_schema.earthquakes
        (magnitude, city, time, updated, detail, longitude, latitude, depth,country, id) 
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING"""
        cursor.execute(insert, (mag, city, time, updated, detail, longitude, latitude, depth, country, id))
        connect.commit()
        print(f"Inserted record {id} into database")


def close_connection():
    if connect:
        cursor = connect.cursor()
        cursor.close()
        connect.close()
        print("PostgreSQL connection is closed")
