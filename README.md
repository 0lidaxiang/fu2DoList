# myCalendar
my to do list, show  my tasks by Calendar style.



# Builld development
## 概念理解
[利用Bootstrap+Vue+Flask 制作一个todolist](https://www.jianshu.com/p/7d8a12674ef0)
[我如何使用 Django + Vue.js 快速构建项目](https://zhuanlan.zhihu.com/p/25080236)

## Install software
[How To Install and Use PostgreSQL on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04)
[PostgreSQL 在Ubuntu上安装指南](http://www.cnblogs.com/bluesfeng/archive/2010/09/01/1815417.html)
[PostgreSQL django 配置](https://realpython.com/deploying-a-django-app-and-postgresql-to-aws-elastic-beanstalk/)
[](https://stackoverflow.com/questions/28611808/how-to-install-psycopg2-for-python-3-5)
```
sudo pip3 install psycopg2
sudo pip3 install psycopg2-binary (another)
```

### PostgreSQL use Introduction
1. show tables & show databases
```
\dt
\l
```

## Django
```
django-admin startproject myproject
python3 manage.py startapp myapp
# modify the models.py
python3 manage.py makemigrations
python3 manage.py migrate
```


## Database
```
create database mycalendar;
create table mycalendar (id  SERIAL PRIMARY KEY, projectId int, task varchar(500), endTime timestamp );
select * from mycalendar;
insert into mycalendar VALUES(2, 1, '工作内容', '2018-05-16 15:36:38');
```
