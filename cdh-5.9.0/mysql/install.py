# -*- coding:utf8 -*-
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd


@roles('mysql')
def install_mysql():
    run('yum install -y mysql-server')


@roles('mysql')
def add_user_and_authorized():
    run("""mysql -u root -p -e \"grant all privileges on *.* to root@'%' identified by 'admin';flush privileges\"""")