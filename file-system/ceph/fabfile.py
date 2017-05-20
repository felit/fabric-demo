# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task, settings,show
from fabric.contrib import files

env.hosts = ['dev@192.168.181.21',
             'dev@192.168.181.22',
             'dev@192.168.181.23',
             'dev@192.168.181.24']

# TODO ceph.conf 改成模板
@task
@parallel
def install():
    with settings(warn_only=True):
        run("ps -ef | grep yum| grep -v grep |awk '{print $2}'| xargs sudo kill -9")
    sudo('yum install -y ceph')
@task
def list():
    with show('hide'):
        run('ls /')