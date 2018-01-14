# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task
from fabric.contrib import files

"""
source /usr/bin/virtualenvwrapper.sh
"""


def install_python27():
    run('wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz')
    run('tar -zxvf Python-2.7.13.tgz')
    with cd('cd Python-2.7.13'):
        run('./configure && make && sudo make install')
    run('wget https://pypi.python.org/packages/11/b6/abcb525026a4be042b486df43905d6893fb04f05aac21c32c638e939e447/pip-9.0.1.tar.gz')
    run('wget https://pypi.python.org/packages/a9/23/720c7558ba6ad3e0f5ad01e0d6ea2288b486da32f053c73e259f7c392042/setuptools-36.0.1.zip')

def install_jupter():
    run('pip install jupyter')


def install_jupter():
    run('pip install virtualenv virtualenvwrapper')


def install_setuptools():
    pass


def intsall_pip():
    pass


def install_sqlite3():
    sudo('yum install -y sqlite sqlite-devel')


def install_libraries():
    """
    安装分析的数据包
    :return:
    """
    run('pip install sqlalchemy pandas numpy matplotlib scikit-learn psycopg2')


def install_nlp():
    """
      自然语言处理
    :return:
    """
    run('pip install nltk nlpir spaCy FastText')


def install_tensorflow():
    run('pip install tensorflow')