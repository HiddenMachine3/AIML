import datetime

import mysql.connector
import matplotlib.dates as mdates
from mysql.connector import Error

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

X = [[55], [60], [61], [70], [80], [90], [95], [100], [101]]
y = [[0], [1], [1], [1], [1], [1], [1], [1], [0]]
classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
classifier.fit(X, y)

# connecting to database
try:
    connection_config_dict = {
        'user': 'root',
        'password': 'mysql_splash',
        'host': '127.0.0.1',
        'database': 'heartdb',
        'raise_on_warnings': True,
        'use_pure': False,
        'autocommit': True,
        'pool_size': 5
    }
    connection = mysql.connector.connect(**connection_config_dict)

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)

        sql_select_Query = "select * from pulsedata"
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        x, y = [], []
        for row in records:
            pulse_value = row[1]
            time = row[0]
            matplotlibdate = mdates.date2num(time)

            x.append(matplotlibdate)
            y.append(pulse_value)
            # X_marks = [[pulse_value]]
            #
            # prediction = classifier.predict(X_marks)
            #
            # text = 'healthy'

            # print(f"time in normal format : {time} = ",end=" ")
            # print(f"time  in   matplotlib : {matplotlibdate}")

        data = pd.DataFrame({
            "time": x,
            "value": y
        })
        plt.plot(data['value'])
        plt.xticks(range(len(data['time'])), data['time'])

        plt.show()
        # while True:
        #     plt.clf()
        #     plt.plot(x, y)
        #     plt.pause(1)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
