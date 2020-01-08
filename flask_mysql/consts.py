# mysql> create database flask_stu charset="utf8mb4";
# mysql> create user 'flask_user'@'localhost' identified by '123456';
# Query OK, 0 rows affected (0.04 sec)
#
# mysql> grant all on flask_stu.* TO 'flask_user'@'localhost';
# Query OK, 0 rows affected (0.01 sec)
# 需要安装赖包
# pip install PyMysql

HOSTNAME = 'localhost'
HOSTNAME_2 = '127.0.0.1'
DATABASE = 'flask_stu'
USERNAME = 'flask_user'
PORT = 3306
PASSWORD = '123456'
DB_URL = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME_2, PORT, DATABASE)  # +MySQLdb
