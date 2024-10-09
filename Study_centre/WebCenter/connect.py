import pymysql
pymysql.install_as_MySQLdb()

conn = pymysql.connect(
      host="rc1d-kk2w92q1pk857nd6.mdb.yandexcloud.net",
      port=3306,
      db="dbcenter",
      user="fursatora",
      passwd="fursatora",
      #ssl={'ca': '/home/fursatora/.mysql/root.crt'}
      )


cur = conn.cursor()
cur.execute('SELECT version()')

print(cur.fetchone()[0])

conn.close()
