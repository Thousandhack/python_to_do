# pip install Flask-MySQLdb
import MySQLdb
from consts import HOSTNAME, DATABASE, USERNAME, PASSWORD

try:
    # 连接数据库
    con = MySQLdb.connect(HOSTNAME, USERNAME, PASSWORD, DATABASE)
    cur = con.cursor()
    # 执行原生数据库的命令
    cur.execute("SELECT VERSION()")
    ver = cur.fetchone()
    print("version:%s" % ver)
except MySQLdb.Error as e:
    print("Error:%s %s" % (e.args[0], e.args[1]))
    exit(1)
finally:
    if con:
        # print("1111")
        con.close()
