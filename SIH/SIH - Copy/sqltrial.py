from flask.ext.mysql import MySQL
from flask import Flask, render_template
app = Flask(__name__)

	


mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'sih'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


conn = mysql.connect()
cursor =conn.cursor()

cursor.execute("SELECT * from trial")
result=cursor.fetchall()
print result
insert_stmt = (
  "INSERT INTO trial (name, age) VALUES (%s, %s)"
)
data = ('Jane', 22)
cursor.execute(insert_stmt, data)
#data = cursor.fetchone()
conn.commit()
#print data