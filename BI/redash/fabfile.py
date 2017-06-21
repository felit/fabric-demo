# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task
from fabric.contrib import files
# TODO
def get_files():
    run('')


def install_requirements():
    run('cd redash-1.0.3')
    run('pip install -r requirements.txt')


def config():
    """
      配置 redash

    """
    run('export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/redash')


def compile():
    """
    　　编译
    　　:return:
    """
    run('cd redash-1.0.3;make')


def migrate():
    """
      TODO 数据迁移任务
      :return:
    """
    run('python manage.py database create_tables')
    run('python manage.py db migrate')


def start_server():
    """

    :return:
    """
    run('python manage.py runserver')


def clear():
    """
    删除redash
    :return:
    """