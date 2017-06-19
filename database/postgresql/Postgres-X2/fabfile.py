# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task
from fabric.contrib import files
# TODO
env.hosts = ['root@139.198.6.107',
             # 'vagrant@192.168.18.190',
]
# env.password = 'vagrant'

def yum():
    sudo('yum install -y wget')


@parallel
def pre_requirement():
    sudo('yum install -y gcc flex bison readline-devel zlib-devel openjade docbook-style-dsssl')


@parallel
def get_tar_files():
    run('wget https://github.com/postgres-x2/postgres-x2/archive/XC1_1_1_PG9_2.tar.gz')
    run('tar -zxvf XC1_1_1_PG9_2.tar.gz')
    run('mkdir /opt/pgxc2')
    run('cd postgres-x2-XC1_1_1_PG9_2; ./configure --prefix=/opt/pgxc2 && make && make install')


@parallel
def add_user_and_groups():
    """
      添加判断
    :return:
    """
    run('groupadd pgxc')
    run('useradd -g pgxc pgxc')
    # run('passwd pgxc')