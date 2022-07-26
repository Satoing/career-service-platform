from config import *
import csv

# city表的数据
with open('../static/data/city.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    cities = [row for row in reader]

# class1表的数据
with open('../static/data/class1.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    class1s = [row for row in reader]

# class2表的数据
with open('../static/data/class2.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    class2s = [row for row in reader]

# salary表的数据
with open('../static/data/salary.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    salaries = [row for row in reader]

# edu表的数据
with open('../static/data/edu.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    edus = [row for row in reader]

# job表的数据
with open('../static/data/job.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    jobs = [row for row in reader]

with open('../static/data/site.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    infos = [row for row in reader]

with open('../static/data/news.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    news = [row for row in reader]

for city in cities:
    db=SQLManager()
    db.create('insert into city values("{}","{}")'.format(city['id'],city['city_name']))

for class1 in class1s:
    db=SQLManager()
    db.create('insert into class1 values("{}","{}")'.format(class1['id'],class1['class_name']))

for class2 in class2s:
    db=SQLManager()
    db.create('insert into class2 values("{}","{}","{}")'.format(class2['id'],class2['class_name'],class2['class1']))

for edu in edus:
    db=SQLManager()
    db.create('insert into edu values("{}","{}")'.format(edu['id'],edu['edu_desc']))

for salary in salaries:
    db=SQLManager()
    db.create('insert into salary values("{}","{}")'.format(salary['id'],salary['salary_desc']))

for job in jobs:
    db = SQLManager()
    db.create('insert into job values("{}","{}","{}","{}","{}","{}","{}")'.format(job['id'], job['title'],job['category'],job['city'],job['salary'],job['edu'],job['company']))

for info in infos:
    db=SQLManager()
    db.create('insert into school values("{}","{}","{}")'.format(info['id'],info['name'],info['site']))

temp=0
for new in news:
    db=SQLManager()
    temp+=1
    db.create('insert into news values("{}","{}","{}","{}")'.format(temp,new['title'],new['url'],new['date']))