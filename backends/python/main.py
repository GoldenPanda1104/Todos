from flask import Flask
from flask_restful import Resource, Api, reqparse
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
api = Api(app)

class mysql():

    def connect(self):
        try:

            
            if mysql.is_connected():
                return mysql
        except Error as e:
            print(e)
    pass
class ToDoItem(Resource):

    def get(self):
        connect = mysql.connector.connect(host='localhost',
                                                    database='todo',
                                                    user='root',
                                                    password='')
        connected = connect.connect()
        cursor = connected.cursor()
        records = cursor.execute("SELECT * FROM todo_item")
        return {'data': records}

    #
    pass

api.add_resource(ToDoItem, '/todos')

if __name__ == '__main__':
    app.run()  # run our Flask app