from flask import Flask
import flask_monitoringdashboard as dashboard

app=Flask(__name__)
dashboard.bind(app)

if __name__ == "__main__":
 app.run(port=5000)