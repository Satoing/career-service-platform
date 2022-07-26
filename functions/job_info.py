from flask import Blueprint, render_template, request
from .config import *

job_info = Blueprint('job_info', __name__)

@job_info.route('/student/job_info')
def std_job_view():
    cook = request.cookies.get('username')
    if cook is None:
        cook = ''

    # 获取查询字符串
    city = request.args.get("city")
    category=request.args.get("category")
    salary=request.args.get("salary")

    flag=None
    if city is not None:flag=0
    elif category is not None:flag=-1
    elif salary is not None:flag=1

    db = SQLManager()
    if flag is None: jobs=db.get_list("select * from job")
    else:
        if flag == 0:
            jobs = db.get_list("select * from job where city='{}'".format(city))
        elif flag < 0:
            jobs = db.get_list("select * from job where category='{}'".format(category))
        elif flag > 0:
            jobs = db.get_list("select * from job where salary='{}'".format(salary))

    for job in jobs:
        job['company']=job['company'][0:7]
        job['category']=db.get_one('select class_name from class2 where id="{}"'.format(job['category']))['class_name']
        job['city'] = db.get_one('select city_name from city where id="{}"'.format(job['city']))['city_name']
        job['salary'] = db.get_one('select salary_desc from salary where id="{}"'.format(job['salary']))['salary_desc']
        job['edu'] = db.get_one('select edu_desc from edu where id="{}"'.format(job['edu']))['edu_desc']

    return render_template('job_info.html',user=cook,jobs=jobs)