# coding=utf-8
HOSTNAME = 'localhost'
HOSTNAME_2 = '127.0.0.1'
DATABASE = 'flask_stu'
USERNAME = 'flask_user'
PORT = 3306
PASSWORD = '123456'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME_2, PORT, DATABASE)  # +MySQLdb

