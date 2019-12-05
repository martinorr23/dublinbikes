# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:25:50 2019

@author: Martin
"""

import psycopg2

def connectToDatabase():
    try:
        dbConnection = psycopg2.connect(
            user="user@dublinbikes",
            password="Password1",
            host="dublinbikes.postgres.database.azure.com",
            port="5432",
            database="dublinbikes")
    except (Exception, psycopg2.Error) as dbError:
        print("Error while connecting to database", dbError)
    return dbConnection

def get_parts():
    """ query parts from the parts table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT part_id, part_name FROM parts ORDER BY part_name")
        rows = cur.fetchall()
        print("The number of parts: ", cur.rowcount)
        for row in rows:
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()