from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@localhost:3306/jobs'
# 协议：mysql+pymysql
# 用户名：root
# 密码：123
# IP地址：localhost
# 端口：3306
# 数据库名：jobs 这里的数据库需要提前建好
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db=SQLAlchemy(app)
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True


class User(db.Model):
    # 定义表名
    __tablename__ = 'user'
    # 定义字段
    # db.Column 表示是一个字段
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(16),unique=True)
    password=db.Column(db.String(16), unique=True)

class Info(db.Model):
    # 定义表名
    __tablename__ = 'info'
    # 定义字段
    # db.Column 表示是一个字段
    id = db.Column(db.Integer, primary_key=True)

    category=db.Column(db.Integer,unique=True)
    cat_ratio=db.Column(db.Integer,unique=True)

    salary = db.Column(db.Integer, unique=True)
    salary_ratio=db.Column(db.Integer, unique=True)

    city = db.Column(db.Integer, unique=True)
    city_ratio=db.Column(db.Integer,unique=True)

    major=db.Column(db.String(50), unique=True)
    user=db.Column(db.String(16), unique=True)

class City(db.Model):
    # 定义表名
    __tablename__ = 'city'
    # 定义字段
    # db.Column 表示是一个字段
    id = db.Column(db.Integer, primary_key=True)
    city_name=db.Column(db.String(16),unique=True)

class Class1(db.Model):
    # 定义表名
    __tablename__ = 'class1'
    # 定义字段
    # db.Column 表示是一个字段
    id = db.Column(db.Integer, primary_key=True)
    class_name=db.Column(db.String(16),unique=True)

class Class2(db.Model):
    # 定义表名
    __tablename__ = 'class2'
    # 定义字段
    # db.Column 表示是一个字段
    id = db.Column(db.Integer, primary_key=True)
    class_name=db.Column(db.String(16),unique=True)
    class1=db.Column(db.Integer)

class Edu(db.Model):
    # 定义表名
    __tablename__ = 'edu'
    # 定义字段
    # db.Column 表示是一个字段
    id = db.Column(db.Integer, primary_key=True)
    edu_desc=db.Column(db.String(16),unique=True)

class Salary(db.Model):
    # 定义表名
    __tablename__ = 'salary'
    # 定义字段
    # db.Column 表示是一个字段
    id = db.Column(db.Integer, primary_key=True)
    salary_desc=db.Column(db.String(16),unique=True)

class Job(db.Model):
    # 定义表名
    __tablename__ = 'job'
    # 定义字段
    # db.Column 表示是一个字段
    id = db.Column(db.Integer, primary_key=True)
    job_name=db.Column(db.String(16))
    category = db.Column(db.Integer)
    city = db.Column(db.Integer)
    salary = db.Column(db.Integer)
    edu = db.Column(db.Integer)
    company = db.Column(db.String(16))

class School(db.Model):
    # 定义表名
    __tablename__ = 'school'
    # 定义字段
    # db.Column 表示是一个字段
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(16),unique=True)
    site = db.Column(db.String(255), unique=True)

class News(db.Model):
    # 定义表名
    __tablename__ = 'news'
    # 定义字段
    # db.Column 表示是一个字段
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(255))
    url = db.Column(db.String(255))
    date = db.Column(db.String(16))


db.create_all()