# -*- coding:utf8 -*-
"""
TODO 改成http安装
"""
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, local,task
from fabric.contrib import files

env.hosts=['root@139.198.6.107']
def mount_deploy_disk():
    if not files.exists('/data'):
        run('mkdir /data')
    # run('mount /dev/sdc /data')
    # run('mount /dev/sdb /data')


def install_yum():
    run('yum update -y')
    run('yum -y install wget unzip gcc openssl-devel zlib zlib-devel bind-utils vim git')


def install_python():
    run('tar -zxvf /data/python2.7/Python-2.7.tgz')
    with cd('Python-2.7'):
        run('./configure')
        run('make')
        run('make install')


def install_pre_requirement():
    run('tar -zxvf /data/python2.7/appdirs-1.4.3.tar.gz')
    with cd('appdirs-1.4.3'):
        run('python setup.py install')

    run('tar -zxvf /data/python2.7/packaging-16.8.tar.gz')
    with cd('packaging-16.8'):
        run('python setup.py install')

    run('tar -zxvf /data/python2.7/pyparsing-2.2.0.tar.gz')
    with cd('pyparsing-2.2.0'):
        run('python setup.py install')

    run('tar -zxvf /data/python2.7/six-1.10.0.tar.gz')
    with cd('six-1.10.0'):
        run('python setup.py install')


def install_pip():
    run('unzip /data/python2.7/setuptools-34.3.3.zip')
    with cd('setuptools-34.3.3'):
        run('python setup.py install')

    run('tar -zxvf /data/python2.7/pip-9.0.1.tar.gz')
    with cd('pip-9.0.1'):
        run('python setup.py install')


def install_pip_libraries():
    run('pip install paramiko fabric')


def upload_scripts():
    """
    上传脚本
    :return:
    """
    local('scp -r /data/source/self/fabric-demo root@139.198.6.107:~/')
    # with cd('cdh-5.9.0'):
    #     run('fab deploy')


@runs_once
@task(default=True)
def install():
    execute(mount_deploy_disk)
    execute(install_yum)
    execute(install_python)
    execute(install_pre_requirement)
    execute(install_pip)
    execute(install_pip_libraries)
    execute(upload_scripts)