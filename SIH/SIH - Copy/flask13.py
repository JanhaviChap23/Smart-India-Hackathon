from flask import Flask,request,render_template
from flaskext.mysql import MySQL
mysql=MySQL()

app=Flask(__name__)
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_DB']='names'
app.config['MYSQL_DATABASE_host']='127.0.0.1:3306'
mysql.init_app(app)


@app.route('/',methods=['GET','POST'])
def get_data():
   if request.method=='POST':
      first_name=request.form['sID']
      last_name=request.form['review']
      typeofmeal=request.form.get("country")
      rating = request.form.get("star")
      connection = mysql.get_db()
      cursor = connection.cursor()
      query="INSERT INTO names_tb2(studID,review,Meal,rate) VALUES(%s,%s,%s,%s)"
      cursor.execute(query,(first_name,last_name,typeofmeal,rating))
      connection.commit()
   return render_template("sample.html")

if __name__=='__main__':
    app.run(debug=True,port=8000)         