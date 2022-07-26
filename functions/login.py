from flask import Blueprint, render_template, request,redirect
from .config import *

login = Blueprint('login', __name__)


@login.route("/student/login", methods=['GET', 'POST'])
def login_view():
    if request.method == 'GET':
        cook = request.cookies.get('username')
        if cook is not None:
            return redirect('/student')
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        print('输入username: {}, password: {}'.format(username, password))

        try:
            db = SQLManager()
            pwd = db.get_list('select password from user where username="{}"'.format(username))
            print('查询到的密码为：',pwd)
            if pwd[0]['password'] == password:
                res = redirect('/student')
                res.set_cookie('username', username)
                resp = request.cookies.get('username')
                print('登录成功！COOKIE为{}'.format(resp))
                return res
        except:
            print('登录失败……')
            return redirect('/student/login')
