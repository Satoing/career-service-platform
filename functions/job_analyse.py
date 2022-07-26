from flask import Blueprint, render_template, request,redirect
from .config import *
from functools import cmp_to_key

job_analyse = Blueprint('job_analyse', __name__)
cat_ratio,city_ratio,salary_ratio=0,0,0
category,city,salary=0,0,0


def cmp(x,y):
    sum1,sum2=0,0
    # print(type(x['salary']),x['category'],x['city'],x['salary'],type(salary))
    if str(x['category'])==str(category):
        sum1+=int(cat_ratio)
    if str(x['city']) == str(city):
        sum1 += int(city_ratio)
    if str(x['salary']) == str(category):
        sum1 += int(salary_ratio)
    print('sum1=',sum1)

    if str(y['category'])==str(category): sum2+=int(cat_ratio)
    if str(y['city']) == str(city): sum2 += int(city_ratio)
    if str(y['salary']) == str(category): sum2 += int(salary_ratio)
    print('sum2=', sum2)

    if sum1 > sum2: return -1
    if sum1 < sum2: return 1
    else: return 0

@job_analyse.route('/student/job_analyse',methods=['GET','POST'])
def std_job_analyse_view():
    global cat_ratio,city_ratio,salary_ratio
    global category,city,salary
    if request.method == 'GET':
        cook = request.cookies.get('username')
        if cook is None:
            return redirect('/student/login')
        try:
            db = SQLManager()
            db.get_one('select * from user where user="{}"'.format(cook))
            return redirect('/student/login')
        except:
            return render_template('fill_info.html',user=cook)
    elif request.method == 'POST':
        # 获取用户填写的信息
        major = request.form.get('major')
        category = request.form.get('category')
        cat_ratio = request.form.get('cat_ratio')
        city = request.form.get('city')
        city_ratio = request.form.get('city_ratio')
        salary = request.form.get('salary')
        salary_ratio = request.form.get('salary_ratio')

        if major is None or cat_ratio is None or city_ratio is None or salary_ratio is None:
            return redirect('/student/job_analyse')

        if major=='' or cat_ratio=='' or city_ratio=='' or salary_ratio=='':
            return redirect('/student/job_analyse')

        print('major=',major,'\n','category=',category,'\n','cat_ratio=',cat_ratio,sep='')
        print('city=', city, '\n', 'city_ratio=', city_ratio, '\n', 'salary=', salary,'\n','salary_ratio=', salary_ratio, sep='')

        db=SQLManager()
        jobs=db.get_list('select * from job')
        # print(jobs[0:10])
        #
        # print("=================================================")

        jobs.sort(key=cmp_to_key(cmp))
        # print(jobs[0:10])

        for job in jobs:
            job['company'] = job['company'][0:7]
            job['category'] = db.get_one('select class_name from class2 where id="{}"'.format(job['category']))[
                'class_name']
            job['city'] = db.get_one('select city_name from city where id="{}"'.format(job['city']))['city_name']
            job['salary'] = db.get_one('select salary_desc from salary where id="{}"'.format(job['salary']))[
                'salary_desc']
            job['edu'] = db.get_one('select edu_desc from edu where id="{}"'.format(job['edu']))['edu_desc']

        cook = request.cookies.get('username')
        return render_template('recommend.html',user=cook,jobs=jobs[0:30])