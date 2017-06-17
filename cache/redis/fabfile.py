# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task
from fabric.contrib import files

env.hosts = ['vagrant@192.168.18.190',
             'vagrant@192.168.18.191',
             'vagrant@192.168.18.192',
]
env.password = 'vagrant'
# TODO
@parallel
def pre_requirement():
    sudo('apt install -y git wget gcc')


@parallel
def make():
    run('wget http://download.redis.io/releases/redis-3.2.9.tar.gz')
    run('tar -zxvf redis-3.2.9.tar.gz')
    run('cd redis-3.2.9;make')


def clear():
    run('rm redis-3.2.9.tar.gz')
    run('rm -fr redis-3.2.9')


def install_web():
    run('git clone https://github.com/JoneXiong/PyRedisAdmin.git')


def start_web():
    run('run PyRedisAdmin')
    run('python routes.py')