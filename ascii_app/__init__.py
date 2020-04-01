from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SECRET_KEY"] = "7be29e9d02fb3cde3ffecb87e9"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
db = SQLAlchemy(app)


# create all db tables
@app.before_first_request
def create_tables():
    from ascii_app.models import TextItem
    db.create_all()


from ascii_app import views
