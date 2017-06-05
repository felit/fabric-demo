# -*- coding:utf8 -*-
from fabric.api import run, execute, roles, task


@roles('mysql')
@task(alias='install_mysql')
def install_mysql():
    run('yum install -y mysql-server')
    run('service mysqld start')
    execute(add_user_and_authorized)


@roles('mysql')
@task(alias='add_user_and_authorized')
def add_user_and_authorized():
    run("""mysql -u root -p -e \"grant all privileges on *.* to root@'%' identified by 'admin';flush privileges\"""")
