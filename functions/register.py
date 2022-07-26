from flask import Blueprint, render_template, request,redirect
from .config import *

register = Blueprint('register', __name__)


@register.route("/student/register", methods=['GET', 'POST'])
def register_view():
    if request.method == 'GET':
        cook = request.cookies.get('username')
        if cook is not None:
            return redirect('/student')
        return render_template('register.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username=='' or password=='' or username is None or password is None:
            redirect('/student/register')
        # print("username=",username)
        # print("password=", password)

        # 插入数据库
        try:
            db = SQLManager()
            count = db.get_one('select count(*) as num from user')['num'] + 1
            db.create('insert into user values("{}","{}","{}")'.format(count, username, password))
        except:
            return redirect('/student/register')
        return redirect('/student/login')
