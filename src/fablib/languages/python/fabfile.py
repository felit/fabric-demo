# -*- coding:utf8 -*-
"""
使用
from languages.python import fabfile as python
python.install()
TODO
添加python3安装
把python添加至sudo路径
"""
from __future__ import with_statement

from fabric.api import run, env, parallel, sudo, cd, task,settings

from src.fablib.common.linux import fabfile as linux


# env.hosts = ['root@www.livedrof.com','root@139.198.6.107']
env.hosts = [
    'vagrant@192.168.18.164',
    # 'vagrant@192.168.18.190'
]
env.password = 'vagrant'
python_url = 'https://www.python.org/ftp/python/2.7.5/Python-2.7.5.tgz'


def pre_requirement():
    """
        添加判断
        :return:
    """
    if linux.is_centos():
        with settings(warn_only=True):
            sudo('yum install -y wget unzip')
    elif linux.is_ubuntu():
        with settings(warn_only=True):
            sudo('apt install -y wget unzip')

@task
@parallel
def install():
    pre_requirement()
    # execute(install_python)
    install_basic_libraries()

def install_python():
    run("wget {python_url} -O python.tar.gz".format(python_url=python_url))
    run("tar -zxvf python.tar.gz")
    dir = run("tar -tf python.tar.gz | awk -F/ '{print $1}' | tail -n 1",shell=False)
    with cd(dir):
        run('./configure')
        run('make')
        sudo('make install')
    run('rm python.tar.gz')
    run('rm -fr %s' % dir)


def install_basic_libraries():
    install_appdirs()
    install_setuptools()
    install_pip()


def install_appdirs():
    run('wget https://pypi.python.org/packages/48/69/d87c60746b393309ca30761f8e2b49473d43450b150cb08f3c6df5c11be5/appdirs-1.4.3.tar.gz -O appdirs.tar.gz')
    run('tar -zxvf appdirs.tar.gz')
    dir = run("tar -tf appdirs.tar.gz | awk -F/ '{print $1}' | tail -n 1")
    with cd(dir):
        sudo('/usr/local/bin/python setup.py install')
    run('rm appdirs.tar.gz')
    sudo('rm -fr %s' % dir)


def install_setuptools():
    run('wget https://pypi.python.org/packages/a9/23/720c7558ba6ad3e0f5ad01e0d6ea2288b486da32f053c73e259f7c392042/setuptools-36.0.1.zip -O setuptools.zip')
    run('unzip setuptools.zip')
    dir = run("unzip -v setuptools.zip | grep setuptools |awk '{print $8}'| tail -1| awk -F/ '{print $1}'")
    with cd(dir):
        sudo('/usr/local/bin/python setup.py install')
    run('rm setuptools.zip')
    sudo('rm -fr %s' % dir)

@task
def install_pip():
    run('wget https://pypi.python.org/packages/11/b6/abcb525026a4be042b486df43905d6893fb04f05aac21c32c638e939e447/pip-9.0.1.tar.gz -O pip.tar.gz')
    run('tar -zxvf pip.tar.gz')
    dir = run("tar -tf pip.tar.gz | awk -F/ '{print $1}' | tail -n 1")
    with cd(dir):
        sudo('/usr/local/bin/python setup.py install')
    run('rm pip.tar.gz')
    sudo('rm -fr %s' % dir)


def has_python():
    pass


def python_version():
    run('python --version')


def install_virtualenv():
    """
    pip位置有问题
    :return:
    """
    sudo('pip install virtualenv virtualenvwrapper')


def clean():
    pass