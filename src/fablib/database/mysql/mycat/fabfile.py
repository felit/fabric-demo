# -*- coding:utf8 -*-
"""

"""

from __future__ import with_statement

from fabric.api import run, env, task, sudo

from src.fablib.common.linux import fabfile as linux


env.hosts = [
    'vagrant@192.168.18.164',
    'vagrant@192.168.18.190'
]
env.password = 'vagrant'


@task
def install():
    add_user_and_group()
    ins()


def add_user_and_group():
    if not linux.has_user('mycat'):
        sudo('useradd mycat')


def ins():
    run('wget http://dl.mycat.io/1.6-RELEASE/Mycat-server-1.6-RELEASE-20161028204710-linux.tar.gz -O mycat.tar.gz')
    run('tar -zxvf mycat.tar.gz')
    dir = run("tar -tf mycat.tar.gz | awk -F/ '{print $1}' | tail -n 1")
    run('mv %s /opt/mycat' % dir)
    sudo('chown -R mycat:mycat /opt/mycat/')


