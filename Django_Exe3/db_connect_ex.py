import pymysql

host ="localhost"
id="root"
pw="system"
db_name="mydb"

#connection 객체 생성
conn=pymysql.connect(host=host, user=id, password=pw,db=db_name, charset='utf8')
print('connected')

#cursor 객체 생성
curs=conn.cursor()

#객체 close
curs.close()
print('closed')