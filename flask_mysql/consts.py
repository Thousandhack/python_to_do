# mysql> create database flask_stu charset="utf8mb4";
# mysql> create user 'flask_user'@'localhost' identified by '123456';
# Query OK, 0 rows affected (0.04 sec)
#
# mysql> grant all on flask_stu.* TO 'flask_user'@'localhost';
# Query OK, 0 rows affected (0.01 sec)

HOSTNAME = 'localhost'
DATABASE = 'flask_stu'
USERNAME = 'flask_user'
PASSWORD = '123456'
DB_URL = 'mysql://{}:{}:@{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, DATABASE)
