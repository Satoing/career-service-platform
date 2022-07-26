from flask import Flask, render_template,request, Response, make_response,redirect
from functions import login,job_info,job_analyse,school,policy,register
from functions.config import SQLManager

# 实例化并命名为app实例
app = Flask(__name__,
            static_folder='static',  # 配置静态文件的文件夹
            template_folder='templates')


# 一些简单界面的路由
@app.route('/')
def index_view():
    return render_template('index.html')

@app.route('/info')
def info_view():
    return render_template('info.html')

@app.route('/echarts')
def echarts():
    return render_template('echarts.html')

@app.route('/student')
def student_view():
    cook=request.cookies.get('username')
    if cook is None:
        cook=''
    return render_template('student.html',user=cook)

@app.route('/student/job_info/city')
def city_view():
    cook=request.cookies.get('username')
    if cook is None:
        cook=''
    return render_template('city.html',user=cook)

@app.route('/student/job_info/salary')
def salary_view():
    cook=request.cookies.get('username')
    if cook is None:
        cook=''
    return render_template('salary.html',user=cook)

@app.route('/student/job_info/category')
def category_view():
    cook=request.cookies.get('username')
    if cook is None:
        cook=''
    return render_template('category.html',user=cook)

@app.route('/student/job_info/class/<cate>')
def cate_view(cate):
    a=SQLManager()
    i=a.get_one('select id from class where class_name="{}"'.format(cate))['id']
    return redirect('/student/job_info?category={}'.format(i))

# 引入蓝图对象
app.register_blueprint(login.login)
app.register_blueprint(job_info.job_info)
app.register_blueprint(job_analyse.job_analyse)
app.register_blueprint(school.school)
app.register_blueprint(policy.policy)
app.register_blueprint(register.register)

# 调用run方法，设定端口号，启动服务
if __name__ == "__main__":
    app.run(port=2022, host="0.0.0.0", debug=True)
