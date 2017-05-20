# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task, settings, show
from fabric.contrib import files

env.hosts = ['dev@192.168.181.21',
             'dev@192.168.181.22',
             'dev@192.168.181.23',
             'dev@192.168.181.24']


@task
@parallel
def install_go():
    sudo('yum install -y go')


@task
@parallel
def status():
    """
    挂载glusterfs文件系统
    :return:
    """
    # TODO 报错
    with settings(warnging_only=True):
        sudo('mkdir /gfs')
        sudo('chown -R dev:dev /gfs')
        sudo('mount -t glusterfs 192.168.181.21:/gv0 /gfs')
    run('ls /gfs')
