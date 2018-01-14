# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task, settings, show
from fabric.contrib import files

env.hosts = ['dev@192.168.181.21',
             'dev@192.168.181.22',
             'dev@192.168.181.23',
             'dev@192.168.181.24']


@task
def add_repo():
    sudo('curl "http://ppa.moosefs.com/MooseFS-2-el6.repo" > /etc/yum.repos.d/MooseFS.repo')